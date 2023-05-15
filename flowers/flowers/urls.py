"""flowers URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from flowersapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('catalog/<str:order>/<int:filter>', views.catalog, name='catalog'),
    path('catalog/<int:id>', views.product_detail, name='product_detail'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('cart', views.cart, name='cart'),
    path('cart_add/<int:id>', views.cart_add, name='cart_add'),
    path('cart_sub/<int:id>', views.cart_sub, name='cart_sub'),
    path('create_order', views.create_order, name='create_order'),
    path('create_order_ajax', views.create_order_ajax, name='create_order_ajax'),
    path('orders', views.orders, name='orders'),
    path('delete_order/<int:id>', views.delete_order, name='delete_order'),
    path('delete_order_ok/<int:id>', views.delete_order_ok, name='delete_order_ok'),
    path('accounts/registration', views.registration, name='registration'),
    path('about/', views.aboutus, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Админ панель'
admin.site.site_title = 'Админка'
admin.site.index_title = 'Добро пожаловать в админку'