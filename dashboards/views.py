from django.shortcuts import render,redirect
from blogs.models import Category, blogs
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm,blogsForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    Category_count = Category.objects.all().count()
    blogs_count = blogs.objects.all().count()
    # print(Category_count)
    # print(blogs_count)
    context = {
        'Category_count':Category_count,
        'blogs_count':blogs_count
    }

    return render(request, 'dashboard/dashboard.html',context)


# categories

def categories(request):
    return render(request, 'dashboard/categories.html')

# add_categories

def add_categories(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form= CategoryForm()
    content = {
        'form':form
    }
    return render(request, 'dashboard/add_categories.html',content)

# edit_categories

def edit_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form= CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context ={
        'form':form,
        'category':category,
    }
    return render(request,'dashboard/edit_categories.html',context)

# delete_categories

def delete_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
# ------------------------------------------------------------------------------------------------------
# POST 

def posts(request):
    posts = blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/post.html',context)

# add_posts

def add_posts(request):
    if request.method == "POST":
        form = blogsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            title = form.cleaned_data['title']
            post.author = request.user
            post.save()
            print("Success") 
            return redirect('posts')
    else: 
        form = blogsForm()
    
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_posts.html', context)

# edit_posts

def edit_posts(request, pk):
    post = get_object_or_404(blogs, pk=pk)
    if request.method == 'POST':
        form= blogsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = blogsForm(instance=post)
    context ={
        'post':post,
        'form':form,
    }
    return render(request,'dashboard/edit_posts.html',context)

# delete_posts

def delete_posts(request,pk):
    post = get_object_or_404(blogs, pk=pk)
    post.delete()
    return redirect('posts')

# user

def users(request):
    users = User.objects.all()
    context = {
        'users':users

    }
    return render(request,'dashboard/users.html',context)

# add_users

def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_users.html',context)

# edit_users

def edit_users(request,pk):
    users = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form= AddUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm(instance=users)
    context ={
        'users':users,
        'form':form,
    }
    return render(request,'dashboard/edit_users.html',context)

# delete_users 

def delete_users(request,pk):
    users = get_object_or_404(User, pk=pk)
    users.delete()
    return redirect('users')