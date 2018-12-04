from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import RegistrationForm,UserUpdateForm,ProfileUpdateForm
# RegistrationProfile
from blog.models import Post,Log
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
# Create your views here.
def register(request):
    form = RegistrationForm()
    # p_form = RegistrationProfile()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)   
        # p_form = RegistrationProfile(request.POST)
        if form.is_valid():
            form.save()
            # p_form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,f'Account created for {username}!')
            messages.success(request,f'Account created for {email}!')
            return redirect('blog-home')
        else:
            form = RegistrationForm()
            # p_form = RegistrationProfile()
    return render(request,'users/masuk.html',{'form':form})
@login_required
def profile(request):
    # username = request.user.username
    context = {
        'posts': Post.objects.filter(idUsers = request.user.pk).order_by('-createdDate'),
        'logs' : Log.objects.filter(idPostUser = request.user.pk),
    }    
    return render(request,'users/profile.html',context)
@login_required
def edit_profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # pas_form = PasswordChangeForm(data=request.POST, user=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # pas_form.save()
            # update_session_auth_hash(request, form.user)
            messages.success(request, f'Your account has been updated!')
            return redirect('blog-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # pas_form = PasswordChangeForm(user=request.user)
    context = {
        'u_form':u_form,
        'p_form':p_form,
        # 'pas_form':pas_form
    }
    return render(request,'users/editprofile.html',context)