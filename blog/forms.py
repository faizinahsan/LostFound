from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','area','image','latitude','longitude','state','idCategories','idTypes')