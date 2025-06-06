from rest_framework import serializers
from .models import Profile, Category, Product, Order, OrderItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# class ProductSerializer(serializers.ModelSerializer):
#     categories = CategorySerializer(many=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'price', 'categories']

class ProductSerializer(serializers.ModelSerializer):
    # Поле categories для чтения (отображения)
    categories = CategorySerializer(many=True, read_only=True)
    # Поле для записи (при создании/обновлении)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='categories',
        many=True,
        required=False  # Делаем необязательным
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'categories', 'category_ids']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = OrderItemSerializer(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'items']
