from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from caropa_app.serializers import SaleSerializer
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalhttp import HttpError
from .paypal_client import PayPalClient

@api_view(['POST'])
def capture_order(request):
    """
    Captures a PayPal order and saves the sale details if the capture is successful.

    Expects a POST request with a JSON body containing the orderID and sale details.
    Returns a confirmation message if the payment is captured and sale details are saved successfully.

    Args:
        request (Request): The HTTP request containing the orderID and sale details.

    Returns:
        Response: A response object with the status of the capture and sale saving process.
    """
    request_body = request.data
    order_id = request_body['orderID']
    paypal_client = PayPalClient()

    capture_request = OrdersCaptureRequest(order_id)

    try:
        response = paypal_client.client.execute(capture_request)
        if response.result.status == "COMPLETED":
            # If payment is captured successfully, save the sale details
            serializer = SaleSerializer(data=request_body)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Payment captured and sale saved successfully!'}, status=200)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({'error': 'Payment not completed'}, status=400)
    except HttpError as error:
        return Response({'error': str(error)}, status=500)
