from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views as rf_views
from drf_yasg import openapi
from rest_framework import routers

from django.urls import path, re_path
from .views import UserDetailView, RegisterView

schema_view = get_schema_view(
    openapi.Info(
        title="BioAPI",
        default_version='v1',
        description="BioAPI, api para usar todos os recursos do BioConecta",
        contact=openapi.Contact(email="saparavaldeir@gmail.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', rf_views.obtain_auth_token),  # Endpoint para obter o token
]


#Swagger
urlpatterns +=[
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]