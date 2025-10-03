from django.shortcuts import render
from .forms import PatientForm
from django.contrib import messages
from .models import Patient

# Create your views here.

def home(request):
    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Patient created successfuly.")
    
    else:
        #when page lpoads (GET request)
        form = PatientForm()
        
    # outside if statement
    patients = Patient.objects.all()



    return render(request, "public/index.html", {"form" : form, "patients" : patients})
    


# def warning(request):
#     return render(request, )


