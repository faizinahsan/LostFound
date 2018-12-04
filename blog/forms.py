from django import forms
from .models import Post,Log, MyModel

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','image','idCategories','idTypes','latitude','longitude')
        # print (fields[5])
        # fields = ('title', 'body','area','image','latitude','longitude','state','idCategories','idTypes')

class PostLogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('body','idUsers','idPosts')
        widgets= {
            'body':forms.HiddenInput(),
            'idPosts': forms.HiddenInput()
        }
class MyModelForm(forms.ModelForm):
    class Meta:
        fields = ('location', 'location_lat', 'location_lon', )
        model = MyModel
