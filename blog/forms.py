from django import forms
from .models import Post,Log

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','image','idCategories','idTypes')
        # fields = ('title', 'body','area','image','latitude','longitude','state','idCategories','idTypes')
class PostLogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('body','idUsers','idPosts')
        widgets= {
            'body':forms.HiddenInput(),
            'idPosts': forms.HiddenInput()
        }