from django.shortcuts import render, HttpResponse , redirect
from blogs.models import Category,blogs
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories  = Category.objects.all()
    featured_post = blogs.objects.filter(is_feacherd=True, status='published')
    posts = blogs.objects.filter(is_feacherd=False , status='published')
    print(posts)
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request, 'home.html',context)

# Register

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    
    else:
        form = RegistrationForm()
    context ={
        'form':form
    }
    return render(request,'register.html',context)

# Login
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(password)
            # print(username)
            user = auth.authenticate(username=username, password= password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    form = AuthenticationForm()
    context ={
        'form':form
    }

    return render(request,'login.html',context)

# logout

def logout(request):
    auth.logout(request)
    return redirect('home')
