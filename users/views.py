from django.shortcuts import render,redirect
from django.contrib import messages
# from users.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,f'Account created for {username}!')
            messages.success(request,f'Account created for {email}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request,'users/masuk.html',{'form':form})
