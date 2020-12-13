from django.urls import path
from . import views 
from .views import ProductSearchResultsView



urlpatterns = [
    path('', views.product_list, name='products'),
    path('<uuid:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/search/', ProductSearchResultsView.as_view(), name='product_search'),


]
