from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # 'cats/' - Cats Index Route
  path('cats/', views.cats_index, name='cats_index'),
  
]