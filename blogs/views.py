from django.shortcuts import render,HttpResponse, redirect
from . models import blogs, Category
from django.shortcuts import get_object_or_404
from .models import blogs as BlogModel 
from django.db.models import Q

# Create your views here.
def posts_by_category(request,category_id):
    posts = BlogModel.objects.filter(status='published', Category= category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # print(posts)

    context = { 
        'posts':posts,
        'category':category
    }
    return render(request, 'posts_by_category.html', context)

# blogs

def blogs(request, slug):
    single_post = get_object_or_404(BlogModel, slug = slug, status= 'published')
    context = {
        'single_post':single_post
    }
    return render(request,'blogs.html',context)

# Search

def search(request):
    keyword = request.GET.get('keyword')
    blog = BlogModel.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains= keyword) | Q(blog_body__icontains = keyword), status='published')
    # print("Value :", blog)
    context = {
        'blog':blog,
        'keyword':keyword
    }
    return render(request,'search.html',context)

