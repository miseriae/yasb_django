from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, PostUpdateForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm 
    template_name = 'update-post.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
