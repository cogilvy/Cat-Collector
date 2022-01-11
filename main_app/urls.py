from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # 'cats/' - Cats Index Route
  path('cats/', views.cats_index, name='cats_index'),
  
  # 'cats/<int:cat_id>/' - Cats Details Route
  path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),

  # 'cats/create/' - Cats Create Route
  path('cats/create/', views.CatCreate.as_view(), name='cats_create'),

  # 'cats/<int:pk>/update/ - Cats Update Route
  path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),

  # 'cats/<int:pk>/delete/ - Cats Delete Route
  path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
]
