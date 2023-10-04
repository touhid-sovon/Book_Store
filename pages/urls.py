from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='home'),
    path('about/',views.AboutTemplateView.as_view(),name='about'),
]