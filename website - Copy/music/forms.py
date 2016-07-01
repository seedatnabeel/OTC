from django import forms
from music.models import Post

class PostForm(forms.ModelForm):
    Cough = forms.BooleanField()
    Fever = forms.BooleanField()
    Runny_Nose = forms.BooleanField()
    Muscle_Pain = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "title",
            "content"
        ]