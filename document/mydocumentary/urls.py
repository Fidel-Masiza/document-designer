from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover_letter_list, name='cover_letter_list'),
    path('create-cover-letter/', views.create_cover_letter, name='create_cover_letter'),
]
