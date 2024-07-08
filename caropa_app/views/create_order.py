from rest_framework.decorators import api_view
from rest_framework.response import Response
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError
from .paypal_client import PayPalClient

@api_view(['POST'])
def create_order(request):
    """
    Creates a PayPal order.

    Expects a POST request with a JSON body containing the amount.
    Returns the PayPal order ID and approval URL if successful.

    Args:
        request (Request): The HTTP request containing the amount.

    Returns:
        Response: A response object with the PayPal order ID and approval URL if successful,
                  or an error message if the creation fails.
    """
    request_body = request.data
    paypal_client = PayPalClient()

    order_request = OrdersCreateRequest()
    order_request.prefer('return=representation')
    order_request.request_body({
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": request_body["amount"]
            }
        }]
    })

    try:
        response = paypal_client.client.execute(order_request)
        order_id = response.result.id
        approval_url = next(link.href for link in response.result.links if link.rel == 'approve')
        return Response({'orderID': order_id, 'approval_url': approval_url})
    except HttpError as error:
        return Response({'error': str(error)}, status=500)
