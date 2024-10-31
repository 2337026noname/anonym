
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('input/', views.input, name='input'),
    path('create/', views.create, name='create'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('editform/<int:post_id>/', views.editform, name='editform'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
]
