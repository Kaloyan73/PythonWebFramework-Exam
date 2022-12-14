from django.conf import settings
from django.urls import path
from .views import store, cart, checkout, update_item, process_order, login_page, register_page
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

    path('update_item/', update_item, name='update_item'),
    path('process_order/', process_order, name='process_order'),
]
