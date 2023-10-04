from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Book

from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)

from django.db.models import Q
# Create your views here.
class BooksListView(LoginRequiredMixin ,ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    login_url = 'account_login'

class BooksDetailView(LoginRequiredMixin ,PermissionRequiredMixin ,DetailView):
    model = Book
    context_object_name = "book"
    template_name ='books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
    queryset = Book.objects.all().prefetch_related('reviews__author',)

class SearchListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search_result.html'
    # queryset = Book.objects.filter(title__icontains = "Opekkha")

    # def get_queryset(self):
    #     return Book.objects.filter(
    #         Q(title__icontains = 'Himu') | Q(title__icontains = 'Dipu')
    #     )
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains = query) | Q(author__icontains=query)
        )