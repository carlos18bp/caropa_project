from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from caropa_app.models import Category
from caropa_app.serializers import CategorySerializer

@api_view(['GET'])
def category_list(request):
    """
    Retrieve all categories.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
