from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # General
    Nausea = forms.BooleanField()
    Body_Aches = forms.BooleanField()
    Chills = forms.BooleanField()
    Fatigue = forms.BooleanField()

    # Head
    Runny_Nose = forms.BooleanField()
    Sore_Throat = forms.BooleanField()
    Cough = forms.BooleanField()
    Nasal_Congestion = forms.BooleanField()
    Headache = forms.BooleanField()
    Sneezing = forms.BooleanField()
    Fever = forms.BooleanField()

    Eye_Redness = forms.BooleanField()
    Eye_Itchiness = forms.BooleanField()
    Eye_Gritty = forms.BooleanField()
    Eye_Discharge = forms.BooleanField()
    Eye_Tearing = forms.BooleanField()
    Itchy_Nose_Mouth_Throat = forms.BooleanField()
    Eyes_Swollen = forms.BooleanField()
    Postnasal_Drip = forms.BooleanField()
    Mucus_White = forms.BooleanField()
    Mucus_GreenYellow = forms.BooleanField()

    # Chest
    Heartburn = forms.BooleanField()
    Vomiting = forms.BooleanField()

    # Abdomen
 #   Indigestion = forms.BooleanField()
    Diarrhoea = forms.BooleanField()
    Abdominal_Cramps = forms.BooleanField()

    # Limbs
    Sore_Joint = forms.BooleanField()
    Sore_Muscles = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "title",
            "content"
        ]