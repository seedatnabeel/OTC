# from django.db import models
#
# class Symptoms(models.Model):
#     sympt = models.CharField(max_length=100)
#     sym = models.BooleanField()


from django.db import models
class Symptoms(models.Model):
    sympt = models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=128)
    content=models.TextField()

    #########
    # General
    Nausea = models.BooleanField()
    Body_Aches = models.BooleanField()
    Chills = models.BooleanField()
    Fatigue = models.BooleanField()

    # Head
    Runny_Nose = models.BooleanField()
    Sore_Throat = models.BooleanField()
    Cough = models.BooleanField()
    Nasal_Congestion = models.BooleanField()
    Headache = models.BooleanField()
    Sneezing = models.BooleanField()
    Fever = models.BooleanField()

    Eye_Redness = models.BooleanField()
    Eye_Itchiness = models.BooleanField()
    Eye_Gritty = models.BooleanField()
    Eye_Discharge = models.BooleanField()
    Eye_Tearing = models.BooleanField()
    Itchy_Nose_Mouth_Throat = models.BooleanField()
    Eyes_Swollen = models.BooleanField()
    Postnasal_Drip = models.BooleanField()
    Mucus_White = models.BooleanField()
    Mucus_GreenYellow = models.BooleanField()


    # Chest
    Heartburn = models.BooleanField()
    Regurgitation = models.BooleanField()

    # Abdomen
    Indigestion = models.BooleanField()
    Diarrhoea = models.BooleanField()
    Abdominal_Cramps = models.BooleanField()

    # Limbs
    Sore_Joint = models.BooleanField()
    Sore_Muscles = models.BooleanField()


    def __unicode__(self):
        return self.title

    def _str_(self):
        return self.title
