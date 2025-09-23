from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo



def helloAdmin(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})


def about(request):
    return render(request, 'about.html')

def learn(request):
    return render(request, 'learn.html')

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.error(request,("ورود ناموفق"))
            return redirect("login")

    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("شما خارج شدید !"))
    return redirect("home")

def signup_user(request):
    
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            
            messages.success(request, ("حساب کاربری با موفیت ساخته شد"))

            return redirect("update_info")
        else:
            print(form.errors)
            messages.success(request, ('مشکلی در ثبت نام وجود دارد'))
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form':form})
    
def update_user(request):

    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد')
            return redirect('home')
        return render(request, 'update_user.html', {'user_form':user_form})
    
    else:
        messages.success(request, 'ابتدا باید وارد حساب کاربری شوید')
        return redirect('home')
    
def update_password(request):

    if request.user.is_authenticated:
        current_user = request.user

        if request.method=='POST':
            form = UpdatePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form})
    else:
        messages.success(request, 'باید اول لاگین کنید')
        return redirect('login')

def update_info(request):

    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None, instance = current_user)

        if form.is_valid():
            form.save()
            
            messages.success(request, 'اطلاعات تکمیلی شما ویرایش شد')
            return redirect('home')
        return render(request, 'update_info.html', {'form':form})
    
    else:
        messages.success(request, 'ابتدا باید وارد حساب کاربری شوید')
        return redirect('home')
    

    


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, cat):
    cat = cat.replace("-"," ")
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html', {'products':products, "category":category})
    except:
        messages.success(request, ('دسته بندی وجود ندارد'))
        return redirect("home")
    
def category_summary(request):
    all_cat = Category.objects.all()
    return render(request, 'category_summary.html', {'category':all_cat})