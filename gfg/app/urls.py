from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('add/', views.create_view, name='create'),
    path('<id>/', views.detail_view, name='detail'),
    path('<id>/update/', views.update_view, name='update'),
     path('<id>/delete/', views.delete_view, name="delete" ),
]
