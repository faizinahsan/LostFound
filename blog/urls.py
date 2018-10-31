from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='blog-home'),
    path('kategori/', views.kategori,name='blog-kategori'),
    path('masuk/', views.masuk ,name='blog-masuk'),
]
