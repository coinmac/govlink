from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from django.views import generic
from ckeditor.widgets import CKEditorWidget


# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'govlink/home.html'
    context_object_name= 'posts'
    
    paginate_by='5'

class CourseCategory(ListView):
    model = Category
    template_name = 'govlink/course_categories.html'
    context_object_name= 'categories'
    
    
    
class CategoryCreate(CreateView):
     model=Category
     fields = ( 'category', 'logo', 'creator')
     
     def form_valid(self, form):
         form.instance.author = self.request.user
         form.save
         return super(CategoryCreate, self).form_valid(form)


class PostCreate(CreateView):
     model=Post
     fields = ( 'category', 'coursename', 'amount', 'content', 'img', 'author', 'popular', 'date_1', 'date_2', 'date_3', 'date_4', 'date_5', 'date_6', 'date_7', 'date_8', )
     
     def form_valid(self, form):
         form.instance.author = self.request.user
         form.save
         return super(PostCreate, self).form_valid(form)


class CourseList(generic.DetailView):
    model = Category
    template_name = 'govlink/course_list.html'
       
