from django.shortcuts import render,redirect
from store.models import *
from .forms import *

# Create your views here.
def home(request):
	customers = Customer.objects.all()
	products = Product.objects.all()
	products_category = ProductCategory.objects.all()
	orders = Order.objects.all()
	pending_orders = Order.objects.filter(complete = False)
	completed_orders = Order.objects.filter(complete = True)


	total_customers = customers.count()
	total_products= products.count()
	total_products_category= products_category.count()
	total_orders = orders.count()
	total_pending_orders = pending_orders.count()
	total_completed_orders = completed_orders.count()

	context = {
		'total_customers':total_customers,
		'total_products':total_products,
		'total_products_category':total_products_category,
		'total_orders':total_orders,
		'total_pending_orders':total_pending_orders,
		'total_completed_orders':total_completed_orders,
	}
	return render(request, 'siteAdmin/home.html', context)

def orders_view(request):
	intro = 'Orders'
	orders = Order.objects.all()
	context = {'orders':orders, 'intro':intro}
	return render(request, 'siteAdmin/admin-step.html',context)

def products_view(request):
	intro = 'Products'
	
	products = Product.objects.all()

	context = {'products':products,'intro':intro}
	return render(request, 'siteAdmin/admin-step.html',context)

def customers_view(request):
	intro = 'Customers'
	customers = Customer.objects.all()
	context = {'customers':customers, 'intro':intro}
	return render(request, 'siteAdmin/admin-step.html',context)

def products_category_view(request):
	intro = 'Products Categories'
	categories = ProductCategory.objects.all()
	context = {'categories':categories, 'intro':intro}
	return render(request, 'siteAdmin/admin-step.html', context)


def product_view_detail(request , pk):
	product = Product.objects.get(id = pk)
	context = {'product':product}
	return render(request, 'siteAdmin/admin-detail.html',context)

def order_view_detail(request, pk):
	order = Order.objects.get(id = pk)
	order_item = OrderItem.objects.filter(order=order)

	if order.complete == True:
		shipping_address = ShippingAddress.objects.get(order = order)
	else:
		shipping_address = ''
	
	context = {'order':order, 'order_item':order_item, 'shipping_address':shipping_address}
	return render(request, 'siteAdmin/admin-detail.html',context)

def customer_view_detail(request, pk):
	user = User.objects.get(username = pk)
	customer = Customer.objects.get(user = user.id)

	order = Order.objects.filter(customer = customer)

	shipping_address = ShippingAddress.objects.filter(customer = customer)

	context = {'orders':order, 'customer':customer,'shipping_addresses':shipping_address}
	return render(request, 'siteAdmin/admin-detail.html',context)

# Create Read Update Delete(CRUD) for Products
def create_product(request):
	if request.method == 'POST':
		form = CreteProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('admin_products')

	else:
		form = CreteProductForm()
	context = {'form':form}
	return render(request, 'siteAdmin/create_product.html', context)

def update_product(request, pk):
	product = Product.objects.get(id = pk)
	if request.method == 'POST':
		form = CreteProductForm(request.POST, request.FILES, instance= product)
		if form.is_valid():
			form.save()
			return redirect('admin_products')

	else:
		form = CreteProductForm(instance = product)
	context = {'form':form}
	return render(request, 'siteAdmin/create_product.html', context)

def delete_product(request, pk):
	product = Product.objects.get(id = pk)
	context = {
		'product':product
	}
	if request.method == 'POST':
		product.delete()
		return redirect('admin_products')

	return render(request, 'siteAdmin/delete.html',context)

# CRUD for product category
def create_product_category(request):
	if request.method == 'POST':
		form = ProductCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('admin_products_category')

	else:
		form = ProductCategoryForm()
	context = {'form':form}
	return render(request, 'siteAdmin/product_category.html', context)

def update_product_category(request, pk):
	product_category = ProductCategory.objects.get(id = pk)
	if request.method == 'POST':
		form = ProductCategoryForm(request.POST, instance= product_category)
		if form.is_valid():
			form.save()
			return redirect('admin_products_category')

	else:
		form = ProductCategoryForm(instance = product_category)
	context = {'form':form}
	return render(request, 'siteAdmin/product_category.html', context)

def delete_product_category(request, pk):
	product_category = ProductCategory.objects.get(id = pk)
	context = {
		'product':product_category
	}
	if request.method == 'POST':
		product_category.delete()
		return redirect('admin_products_category')

	return render(request, 'siteAdmin/delete.html',context)


