from django import forms
from blogs.models import Category
from blogs.models import blogs

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields ='__all__'

class blogsForm(forms.ModelForm):
    class Meta:
        model=blogs
        fields =('title','Category','blog_image','short_description','blog_body','status','is_feacherd')