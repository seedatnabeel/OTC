from django import forms
from music.models import Post

class PostForm(forms.ModelForm):
    box = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "title",
            "content"
        ]