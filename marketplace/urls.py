from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf.urls.static import static 
from django.conf import settings

from marketplace_app.views import ProductViewSet, CategoryViewSet
from users.views import UserViewSet, RegisterView, LoginView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
