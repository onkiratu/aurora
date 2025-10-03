from django import forms
from .models import Patient

gender_choices = [("male", "Male"), ("female", "Female")]
race_choices = [("caucasian", "Caucasian" ),("african", "African"), ("asian", "Asian"), ("aboriginal", "Aboriginal")]


# inherit from forms.ModelForm because it is linked to DB if not from forms.Form
class PatientForm(forms.ModelForm): 

    patient_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter patient no"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter first name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter last name"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter age"}))
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select)
    race = forms.ChoiceField(choices=race_choices, widget=forms.Select) 


    class Meta:
        model = Patient
        fields = ["patient_number", "first_name", "last_name", "age", "gender", "race"]


