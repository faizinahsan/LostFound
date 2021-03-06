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
        totalCount = {}
        posts = Post.objects.filter(title__icontains=search_query).order_by('-createdDate')
        for cat in Category.objects.all():
            totalCount[cat] = posts.filter(idCategories=cat.pk).count
        for eachtotal in totalCount :
            print(eachtotal,"=",totalCount[eachtotal])
        context ={
            'posts':posts,
            'typesLost':Post.objects.filter(idTypes=1,title__icontains=search_query),
            'typesFound':Post.objects.filter(idTypes=2,title__icontains=search_query),
            'categories': Category.objects.all(),
            'total':totalCount
        }
        return render(request,'blog/search.html',context)
    return render(request,'blog/search.html',context)
 
def searchCat(request,idCat):
    totalCount = {}
    posts = Post.objects.filter(idCategories=idCat).order_by('-createdDate')
    for cat in Category.objects.all():
        totalCount[cat] = posts.filter(idCategories=cat.pk).count
    context = {
        'posts':posts,
        'typesLost':Post.objects.filter(idTypes=1,idCategories=idCat),
        'typesFound':Post.objects.filter(idTypes=2,idCategories=idCat),
        'total':totalCount
    }
    return render(request,'blog/search.html',context)
def searchTypes(request,idType):
    totalCount = {}
    posts = Post.objects.filter(idTypes=idType).order_by('-createdDate')
    for cat in Category.objects.all():
        totalCount[cat] = posts.filter(idCategories=cat.pk).count
    context = {
        'posts':posts,
        'typesLost':Post.objects.filter(idTypes=1 ),
        'typesFound':Post.objects.filter(idTypes=2),
        'total':totalCount
    }
    return render(request,'blog/search.html',context)
def detailView(request,idPost):
    # form = PostLogForm()
    logs = Log.objects.filter(idUsers = request.user.pk)
    posts = Post.objects.get(pk = idPost)
    logIdUser = 0
    logIdPost = 0
    stateForContact = 0
    for log in logs:
        if log.idUsers.pk == request.user.pk and log.idPosts.pk == posts.pk:
            logIdUser = log.idUsers.pk
            logIdPost = idPost
            stateForContact = 1
        # print("user :",logIdUser)
        # print("post :",logIdPost)
    if request.method == "POST":
        form = PostLogForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('idUsers')
            body = form.cleaned_data.get('body')
            idPosts = form.cleaned_data.get('idPosts')
            idUserPost = form.cleaned_data.get('idUserPost')
            messages.success(request,f'Anda Sekarang dapat melihat kontak orang ini!')
            # messages.success(request,f'Kontak Di Akses Oleh {username}!')
            # messages.success(request,f'Dengan Isi {body}!')
            # messages.success(request,f'Di Post ke {idPosts}!')
            # messages.success(request,f'User yang dilihat adalah {idUserPost}!')
            # return redirect('blog-home')
    else:
        form = PostLogForm()
    # if Log.objects.filter(idUsers = request.user.pk).first
    context={
        'form':form,
        'post':posts,
        'contacts':Log.objects.filter(idPosts = idPost),
        'logs':Log.objects.filter(idUsers = request.user.pk),
        'stateForContact': stateForContact
    }
    return render(request,'blog/detailpost.html',context)
def detailKontakView(request):
    return HttpResponse('<h1>entered text: </h1>'+ request.POST.get['body',False])
def createPost(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
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
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            messages.success(request,f'Form Is Valid')
            post = form.save(commit=False)
            post.idUsers = request.user
            post.save()
            return redirect('blog-deskripsi', idPost=post.pk)
    else:
        messages.success(request,f'Failed to Update Post')
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
