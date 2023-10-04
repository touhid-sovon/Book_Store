from django.urls import path
from . import views


urlpatterns = [
    path('',views.BooksListView.as_view(),name = 'book_list'),
    path('<uuid:pk>/',views.BooksDetailView.as_view(),name='book_detail'),
    path('search/',views.SearchListView.as_view(),name='search_result'),
]