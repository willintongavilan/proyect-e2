"""proyecto URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apphos import views as views_auth


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views_auth.UserCreateView.as_view()),
    path('user/<int:pk>/', views_auth.UserDetailView.as_view()),
    path('product/', views_product.product_api_view),
    path('product/<int:pk>/', views_product.product_detail_view)
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
    ]
#127.0.0.1:8000/api/Paciente

