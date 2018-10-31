from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blog/index.html')
def kategori(request):
    return render(request,'blog/kategori.html')
def masuk(request):
    return render(request,'blog/masuk.html')