from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import RegistrationForm
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    form = RegistrationForm()   
    if request.method == 'POST':
        form = RegistrationForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,f'Account created for {username}!')
            messages.success(request,f'Account created for {email}!')
            return redirect('blog-home')
        else:
            form = RegistrationForm()
    return render(request,'users/masuk.html',{'form':form})

def profile(request):
    # username = request.user.username
    context = {
        'posts': Post.objects.filter(idUsers = request.user.pk).order_by('-createdDate')
    }    
    return render(request,'users/profile.html',context)

def edit_profile(request):
    return render(request,'users/editprofile.html')