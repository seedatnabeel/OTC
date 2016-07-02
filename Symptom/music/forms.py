from django import forms
from music.models import Post

class PostForm(forms.ModelForm):
   # Cough = forms.BooleanField()
    Cough = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit();'}), required=False,label="Status")
    Fever = forms.BooleanField()
    Runny_Nose = forms.BooleanField()
    Nasal_Congestion = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "title",
            "content"
        ]