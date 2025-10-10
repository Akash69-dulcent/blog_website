from django.shortcuts import render,redirect
from blogs.models import Category, blogs
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm
from django.shortcuts import get_object_or_404

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