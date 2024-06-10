from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from caropa_app.models import Home, Banner, HomeCategories
from caropa_app.serializers import HomeSerializer, BannerSerializer, HomeCategoriesSerializer

class HomeDataView(APIView):
    """
    API view to handle GET requests and return the data of Home, Banner, and HomeCategories models.
    """
    def get(self, request):
        # Assuming you have only one Home instance, otherwise adjust the query as needed
        home = Home.objects.first()
        banners = Banner.objects.all()
        home_categories = HomeCategories.objects.all()

        # Serialize the data
        home_serializer = HomeSerializer(home)
        banner_serializer = BannerSerializer(banners, many=True)
        home_categories_serializer = HomeCategoriesSerializer(home_categories, many=True)

        # Combine the serialized data into a single response
        data = {
            'home': home_serializer.data,
            'banners': banner_serializer.data,
            'home_categories': home_categories_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
