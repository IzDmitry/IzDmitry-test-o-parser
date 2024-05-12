from django.contrib import admin
from django.urls import include, path
from products import views as api_products

#from user.views import UserViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'product', api_products.ProductViewSet, basename='ProductViewSet')


schema_view = get_schema_view(
   openapi.Info(
      title='Snippets API',
      default_version='v1',
      description="Test description",
      terms_of_service='https://www.google.com/policies/terms/',
      contact=openapi.Contact(email='contact@snippets.local'),
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),

    path("", include('admin_adminlte.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]