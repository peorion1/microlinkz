from django.urls import path
from .views import index, about_page,operator, home_page, product_list, product_detail, product_create, product_update, product_delete



urlpatterns = [
    path('', index, name="index"),
    path('about/', about_page, name="aboutpage"),
    path('operator/', operator, name="operator"),
    path('home/', home_page, name="homepage"),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]

