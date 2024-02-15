from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    show_product = product.objects.all()
    context  = {"product_data" : show_product}
    return render(request,'product_data.html',context)

def add_product(request):
    context = {"product_type" : d_type.objects.all()}
    if request.method == "POST":
        table = product()
        table.product_name = request.POST['product_name']
        table.product_type = d_type.objects.get(type_id = request.POST['product_type'])
        table.product_qty = request.POST['quantity']
        table.product_exp = request.POST['product_expired']
        table.save()
        return redirect('/manage_product')
    return render(request,'add_product.html',context)


def add_type(request):
    if request.method == "POST":
        table = d_type()
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'add_type.html')

def manage_product(request):
    show_product = product.objects.all()
    context  = {"product" : show_product}
    return render(request,'edit_product.html',context)

def manage_type(request):
    show_type = d_type.objects.all() 
    context  = {"type" : show_type} 
    return render(request,'manage_type.html',context) 



def delete_report(request,pk):
    table = product.objects.get(report_id=pk)
    table.delete()
    return redirect('/buy_product')

def delete_product(request,pk):
    table = product.objects.get(product_id=pk)
    table.delete()
    return redirect('/manage_product')

def delete_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    table.delete()
    return redirect('/manage_type')

@login_required(login_url="/login")
def edit_product(request,pk):
    table = product.objects.get(product_id=pk)
    table2 = d_type.objects.all()
    context = {"product_data" : table , "product_type" : table2}
    if request.method == "POST":
        table.product_name = request.POST['product_name']
        table.product_type = d_type.objects.get(type_id = request.POST['product_type'])
        table.product_qty = request.POST['product_qty']
        table.product_exp = request.POST['product_expired'] 
        table.save()
        return redirect('/manage_product')
    return render(request,'edit_d.html',context)

@login_required(login_url="/login")
def edit_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    context = {"type_data" : table}
    if request.method == "POST":
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'edit_t.html',context)


def increase_product(request,pk):
    print (pk)
    table = product.objects.get(product_id=pk)
    update_qty = table.product_qty+1
    table.product_qty = update_qty
    table.save()
    return redirect('/manage_product') 


def decrease_product(request,pk):
    print (pk)
    table = product.objects.get(product_id=pk)#ORM 
    update_qty = table.product_qty-1
    table.product_qty = update_qty
    table.save()
    return redirect('/manage_product')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return redirect('/login')


from django.shortcuts import get_object_or_404, redirect

def buy_product_view(request):
    show_report = report_buy.objects.all() 
    context  = {"report" : show_report} 
    return render(request, "buy_product.html", context)


@login_required(login_url="/login")
def buy_product(request):
    context = {"userbuy": userbuy.objects.all(), "products": product.objects.all()}
    if request.method == "POST":
        table = report_buy()
        table.username = request.POST.get('Busername')
        table.address = request.POST.get('Baddress')
        table.tal = request.POST.get('Btal')
        table.product_name = request.POST.get('product_name')
        table.product_qty = request.POST.get('quantity')
        table.save()
    return render(request, 'buy_productu.html', context)



from django.contrib.auth.models import User
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        return redirect('/login') 
    return render(request, 'register.html')

def report_a(request):
    show_report = report_buy.objects.all() 
    context  = {"report" : show_report} 
    return render(request,'report_a.html',context) 