"""djangoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from store.views.home_page_view import HomePageView
from checkout.views.cart_view import CartView
from checkout.views.remove_from_cart_view import RemoveFromCartView
from products.views.product_detail_view import ProductDetailView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^product/(?P<pk>\d+)', ProductDetailView.as_view(), name='product'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^cart/', CartView.as_view(), name='cart'),
]
