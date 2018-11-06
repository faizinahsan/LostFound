from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request,'blog/index.html')
def kategori(request):
    return render(request,'blog/kategori.html')
def masuk(request):
    return render(request,'blog/masuk.html')
def dev_post(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/dev_post.html',context)