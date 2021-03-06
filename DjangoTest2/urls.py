"""DjangoTest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from common.views import customer_register
from tes.views import listener
from mgr.views import resdata
# from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', listener),

    path('admin/', admin.site.urls),

    path('test/', listener),

    path('mgrtest/', resdata),

    path('register/', customer_register),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),

    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),

    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

]
