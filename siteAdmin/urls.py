from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name = 'home'),
	path('customers', views.customers_view, name = 'admin_customers'),
	path('products', views.products_view, name = 'admin_products'),
	path('orders', views.orders_view, name = 'admin_orders'),
	path('category', views.products_category_view, name = 'admin_products_category'),

	path('products/create', views.create_product, name = 'create_product'),
	path('products/update/<int:pk>', views.update_product, name = 'update_product'),
	path('products/delete/<int:pk>', views.delete_product, name = 'delete_product'),

	path('customer-detail/<str:pk>', views.customer_view_detail , name = 'customer-detail'),
	path('order-detail/<str:pk>', views.order_view_detail , name = 'order-detail'),
	path('product-detail/<str:pk>', views.product_view_detail , name = 'product-detail'),

	path('category/create', views.create_product_category, name = 'create_product_category'),
	path('category/update/<int:pk>', views.update_product_category, name = 'update_product_category'),
	path('category/delete/<int:pk>', views.delete_product_category, name = 'delete_product_category'),
]