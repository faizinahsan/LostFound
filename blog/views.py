from django.shortcuts import render
from .models import Post,Category,Types
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
def index(request):
    return render(request,'blog/index.html')
def kategori(request):
    context={
        'cat':Category.objects.all()
    }
    return render(request,'blog/kategori.html',context)
def masuk(request):
    return render(request,'blog/masuk.html')
def dev_post(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/dev_post.html',context)
def profile(request):
    return render(request,'blog/profile.html')
def edit_profile(request):
    return render(request,'blog/editprofile.html')
def search(request):
    context ={
        'posts':Post.objects.all(),
        'typesLost':Post.objects.filter(idTypes=1),
        'typesFound':Post.objects.filter(idTypes=2),
    }
    return render(request,'blog/search.html',context)
def searchCat(request,idCat):
    context = {
        'posts':Post.objects.filter(idCategories=idCat),
        'typesLost':Post.objects.filter(idTypes=1,idCategories=idCat),
        'typesFound':Post.objects.filter(idTypes=2,idCategories=idCat),
    }
    return render(request,'blog/search.html',context)
def searchTypes(request,idTypes):
    context = {
        'posts':Post.objects.filter(idCategories=idTypes),
        'typesLost':Post.objects.filter(idTypes=1,idCategories=idTypes),
        'typesFound':Post.objects.filter(idTypes=2,idCategories=idTypes),
    }
    return render(request,'blog/search.html',context)
# class SearchTypes(ListView):
#     model = Post
#     template_name = 'blog/search.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
