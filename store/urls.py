from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from shop.views import (
    UserViewSet, ProfileViewSet, CategoryViewSet,
    ProductViewSet, OrderViewSet, OrderItemViewSet, NameSearchView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Store API",
        default_version='v1',
        description="API for managing users, products, and orders",
    ),
    public=True,
)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger',
#          cache_timeout=0), name='schema-swagger-ui'),
#     path('', TemplateView.as_view(template_name='index.html'), name='home'),
#     path('', NameSearchView.as_view(), name='name-search'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # <--- добавлено
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('search/', NameSearchView.as_view(), name='name-search'),
]
