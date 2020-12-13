from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path('add/<uuid:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('delete_from_list/<uuid:product_id>/', views.delete_from_list, name='delete_from_list'),
]