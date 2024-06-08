from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from caropa_app.models import Product
from caropa_app.serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    """
    Retrieve all products.
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
