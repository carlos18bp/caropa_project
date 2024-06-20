from rest_framework import serializers
from caropa_app.models import Product, Sale, SoldProduct
from caropa_app.serializers import ProductSerializer

class SoldProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the SoldProduct model.

    This serializer converts SoldProduct model instances to JSON format and vice versa.
    It includes a write-only field for the product ID and a read-only nested serializer for the product.
    """
    product_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SoldProduct
        fields = ['product_id', 'product', 'color_selected', 'quantity']

class SaleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sale model.

    This serializer converts Sale model instances to JSON format and vice versa.
    It includes a nested serializer for sold products.
    """
    sold_products = SoldProductSerializer(many=True)

    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        """
        Creates a Sale instance along with its associated SoldProduct instances.

        Args:
            validated_data (dict): The validated data containing the sale and sold products information.
        
        Returns:
            Sale: The created Sale instance.
        """
        sold_products_data = validated_data.pop('sold_products')
        sale = Sale.objects.create(**validated_data)
        for sold_product_data in sold_products_data:
            product_id = sold_product_data.pop('product_id')
            product = Product.objects.get(id=product_id)
            sold_product = SoldProduct.objects.create(product=product, **sold_product_data)
            sale.sold_products.add(sold_product)
        return sale
