from django.urls import path
from . import views
from .models import Post
urlpatterns = [
    path('', views.index,name='blog-home'),
    path('kategori/', views.kategori,name='blog-kategori'),
    path('masuk/', views.masuk ,name='blog-masuk'),
    path('post/', views.dev_post ,name='blog-post'),
    path("search/", views.search, name="blog-search"),
    path("searchCat/<idCat>/", views.searchCat, name="blog-search-cat"),
    path("searchTypes/<idType>/", views.searchTypes, name="blog-search-types"),
    path("deskripsi/<idPost>/", views.detailView, name="blog-deskripsi"),
    path("kontak/", views.detailKontakView, name="blog-kontak"),
    path("create/", views.createPost, name="blog-create"),
    path("create/<int:idPost>/edit", views.editPost, name="blog-edit"),
    path("create/<int:idPost>/delete", views.deletePost, name="blog-delete"),
]
