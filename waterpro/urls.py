"""
URL configuration for waterpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from waterapp.views import index,register,loginview
from waterapp import admin_urls,user_urls

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    path('login/',loginview.as_view()),
    path('register/',register.as_view(),name='register'),
    # path('signup',servicer_signup.as_view(),name='signup'),


   
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
