from django.shortcuts import render,redirect, get_object_or_404
from .models import Post,Category,Types,Log
from django.contrib import messages
from .forms import PostForm, PostLogForm
from django.http import HttpResponse
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
    # form = PostLogForm()
    if request.method == "POST":
        form = PostLogForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('idUsers')
            body = form.cleaned_data.get('body')
            idPosts = form.cleaned_data.get('idPosts')
            idUserPost = form.cleaned_data.get('idUserPost')
            messages.success(request,f'Kontak Di Akses Oleh {username}!')
            messages.success(request,f'Dengan Isi {body}!')
            messages.success(request,f'Di Post ke {idPosts}!')
            messages.success(request,f'User yang dilihat adalah {idUserPost}!')
            # return redirect('blog-home')
    else:
        form = PostLogForm()

    context={
        'form':form,
        'post':Post.objects.get(pk = idPost),
        'contacts':Log.objects.filter(idPosts = idPost),
    }
    return render(request,'blog/detailpost.html',context)
def detailKontakView(request):
    return HttpResponse('<h1>entered text: </h1>'+ request.POST.get['body',False])
def createPost(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.idUsers = request.user
            post.save()
            return redirect('blog-deskripsi',idPost = post.pk)
        else:
            form = PostForm()
    return render(request,'blog/post.html',{'form': form})
# class SearchTypes(ListView):
#     model = Post
#     template_name = 'blog/search.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
def editPost(request,idPost):
    post = get_object_or_404(Post, pk=idPost)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.idUsers = request.user
            post.save()
            return redirect('blog-deskripsi', idPost=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editpost.html', {'form': form,'post':post})
def deletePost(request,idPost):
    post = get_object_or_404(Post, pk=idPost)
    author = post.idUsers.username
    if request.method == "POST" and request.user.is_authenticated and request.user.username == author:
        post.delete()
        messages.success(request,f'Post Successfully Deleted')
        return redirect('blog-home')

    return render(request, 'blog/deletepost.html',{'post':post})