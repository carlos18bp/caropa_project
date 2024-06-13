from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from caropa_app.models import Home, Banner, HomeCategories
from caropa_app.serializers import HomeSerializer, BannerSerializer, HomeCategoriesSerializer

@api_view(['GET'])
def home_data(request):
    """
    Retrieve data for Home, Banner, and HomeCategories models.
    """
    # Assuming you have only one Home instance, otherwise adjust the query as needed
    home = Home.objects.first()
    banners = Banner.objects.all()
    home_categories = HomeCategories.objects.all()

    # Serialize the data
    home_serializer = HomeSerializer(home, context={'request': request})
    banner_serializer = BannerSerializer(banners, many=True, context={'request': request})
    home_categories_serializer = HomeCategoriesSerializer(home_categories, many=True, context={'request': request})

    # Combine the serialized data into a single response
    data = {
        'home': home_serializer.data,
        'banners': banner_serializer.data,
        'home_categories': home_categories_serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)
