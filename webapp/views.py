from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm  

def index(request):
    return render(request, 'pages/index.html')

def operator(request):
    return render(request, 'pages/operator.html')

def about_page(request):
    return render(request, 'pages/aboutpage.html')

def home_page(request):
    products = Product.objects.all()
    return render(request, 'pages/homepage.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pages/product_form.html', {'form': form, 'action': 'Create'})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('pages:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pages/product_form.html', {'form': form, 'action': 'Update'})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'pages/product_confirm_delete.html', {'product': product})

