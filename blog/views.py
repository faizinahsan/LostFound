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

def search(request):
    if request.method =='GET':
        search_query = request.GET.get('search_box', None)
        context ={
            'posts':Post.objects.filter(title__icontains=search_query).order_by('-createdDate'),
            'typesLost':Post.objects.filter(idTypes=1,title__icontains=search_query),
            'typesFound':Post.objects.filter(idTypes=2,title__icontains=search_query),
        }
        return render(request,'blog/search.html',context)
    return render(request,'blog/search.html',context)
def searchCat(request,idCat):
    context = {
        'posts':Post.objects.filter(idCategories=idCat).order_by('-createdDate'),
        'typesLost':Post.objects.filter(idTypes=1,idCategories=idCat),
        'typesFound':Post.objects.filter(idTypes=2,idCategories=idCat),
    }
    return render(request,'blog/search.html',context)
def searchTypes(request,idType):
    context = {
        'posts':Post.objects.filter(idTypes=idType).order_by('-createdDate'),
        'typesLost':Post.objects.filter(idTypes=1 ),
        'typesFound':Post.objects.filter(idTypes=2),
    }
    return render(request,'blog/search.html',context)
def detailView(request,idPost):
    context={
        'post':Post.objects.get(pk = idPost)
    }
    return render(request,'blog/deskripsi.html',context)
# class SearchTypes(ListView):
#     model = Post
#     template_name = 'blog/search.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
