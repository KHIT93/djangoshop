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
from store.views.product_list_view import ProductListView
from checkout.views.cart_view import CartView
from checkout.views.checkout_address_view import CheckoutAddressView
from checkout.views.checkout_confirmation_view import CheckoutConfirmationView
from checkout.views.checkout_completed_view import CheckoutCompletedView
from products.views.product_detail_view import ProductDetailView
from customers.views.myaccount_detail_view import MyAccountDetailView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^product/(?P<pk>\d+)', ProductDetailView.as_view(), name='product'),
    url('^myaccount/$', MyAccountDetailView.as_view(), name='myaccount'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^cart/', CartView.as_view(), name='cart'),
    url(r'^checkout/address', CheckoutAddressView.as_view(), name='checkout_address'),
    url(r'^checkout/confirm', CheckoutConfirmationView.as_view(), name='checkout_confirm'),
    url(r'^checkout/complete', CheckoutCompletedView.as_view(), name='checkout_complete'),
    url(r'^shop/(?P<pk>\d+)', ProductListView.as_view(), name='shop'),
    url(r'^shop/$', ProductListView.as_view(), name='shop'),
]
