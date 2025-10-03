from django.db import models

# Create your models here.
class Patient(models.Model):
    gender_choices = [("male", "Male"), ("female", "Female")]
    race_choices = [("caucasian", "Caucasian" ),("african", "African"), ("asian", "Asian"), ("aboriginal", "Aboriginal")]

    patient_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    race = models.CharField(max_length=10, choices=race_choices)


    def __str__(self):
            return f" {self.first_name} : {self.patient_number} "







    

