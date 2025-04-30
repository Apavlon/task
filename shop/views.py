from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User, Profile, Category, Product, Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import (
    UserSerializer, ProfileSerializer, CategorySerializer,
    ProductSerializer, OrderSerializer, OrderItemSerializer
)
from django.contrib.auth.models import User as AuthUser


@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Разрешить доступ без авторизации

    @swagger_auto_schema(operation_description="Create a new user")
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = request.data.get('username')
        email = request.data.get('email')
        if username and email:
            auth_user, created = AuthUser.objects.get_or_create(
                username=username,
                defaults={'email': email, 'is_staff': True}
            )
            if created:
                auth_user.set_password('defaultpassword')
                auth_user.save()
        from channels.layers import get_channel_layer
        from asgiref.sync import async_to_sync
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'users', {
                'type': 'user_notification',
                'message': f"New user created: {request.data.get('username')}"
            }
        )
        return response


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class NameSearchView(View):
    def get(self, request):
        return HttpResponse("Hello from NameSearchView")
