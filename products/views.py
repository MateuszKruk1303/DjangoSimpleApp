from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm, ProductEditForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')        
def view_products(request):
    products = Products.objects.order_by('id')
    context = {'products': products}
    return render(request, 'products/index.html', context)

@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product = product.save(commit=False)
            product.save()
            return redirect('/products')

@login_required(login_url='/login/')
def delete(request, name):
    model = Products
    model.objects.filter(name=name).delete()
    return redirect('/products/')

@login_required(login_url='/login/')        
def edit_name(request, name):
    model = Products
    form = ProductEditForm(request.POST)
    obj = model.objects.get(name=name)
    obj.name = form.data.get("new_name", "0")
    obj.save()
    return redirect('/products/')