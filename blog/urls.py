from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='blog-home'),
    path('kategori/', views.kategori,name='blog-kategori'),
    path('masuk/', views.masuk ,name='blog-masuk'),
    path('post/', views.dev_post ,name='blog-post'),
    path("profile/", views.profile, name="blog-profile"),
    path("editprofile/", views.edit_profile, name="blog-editprofile"),
    path("search/", views.search, name="blog-search"),
]
