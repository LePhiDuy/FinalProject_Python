from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('category/<slug:category_slug>/', views.list_product, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
]
