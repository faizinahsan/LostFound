from django import forms
# from .models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# class CustomForm(forms.ModelForm):
#     username = forms.CharField(required=False)
#     email = forms.EmailField(label='Your email')
#     password = forms.CharField(max_length = 32, widget=forms.PasswordInput)
# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(max_length = 32, widget=forms.PasswordInput)
#     class Meta:
#         model = Registration
#         fields = ['username','email','password']
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
       model = User
       fields=('username','email','password1','password2')

    def save(self,commit = True):
        user = super(RegistrationForm,self).save(commit = False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save() 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
       model = User
       fields=('first_name','last_name','username','email')
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','line','phone']