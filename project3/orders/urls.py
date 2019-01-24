from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_order/", views.submit_order, name="submit_order"),
    path("confirm_order/", views.confirm_order, name="confirm_order"),
    path('signup/', views.signup, name='signup'),
    path('send_cart/', views.send_cart, name='send_cart'),
    path('<str:username>/get_cart/', views.get_cart, name='get_cart')
]