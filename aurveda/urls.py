"""
URL configuration for aurveda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    
    #Admin urls
    path('index1/',views.index1,name='index1'),
    path('client-profile/',views.client_profile,name='client-profile'),
    path('page-login/',views.page_login,name='page-login'),
    path('send-suggestions/',views.send_suggestions,name='send-suggestions'),
    path('users-profile/',views.users_profile,name='users-profile'),
    path('view_documents/',views.view_documents,name='view-documents'),
    path('view-receive-payment/',views.view_receive_payment,name='view-receive-payment'),
    path('view-suggestions/',views.view_suggestions,name='view-suggestions'),
    
    
    #client urls
    path('index2/',views.client_index,name='index2'),
    path('payment-info/',views.payment_info,name='payment-info'),
    path('profile/',views.profile,name='profile'),
    path('send-document/',views.send_document,name='send-document'),
    path('send-query/',views.send_query,name='send-query'),
    
]
