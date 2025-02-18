from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

# Đăng ký tài khoản
def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # Chuyển hướng sau khi đăng ký
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form})

# Đăng nhập
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})

# Đăng xuất
def user_logout(request):
    logout(request)
    return redirect('book_list')
