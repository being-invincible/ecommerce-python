from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .views import (
    welcome,
    login,
    login_user,
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
)

app_name = 'core'

urlpatterns = [
    # path('', welcome, name='welcome'),
    # path('login/', login, name='login'),
    # path('login-user/', login_user),'''
    path('', login_required(csrf_exempt(HomeView.as_view())), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
