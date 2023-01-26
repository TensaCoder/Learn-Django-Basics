from django.shortcuts import render, HttpResponse
from datetime import datetime
from main.models import Contact

# Create your views here.

def home(request):
    context = {
        "string" : "Herschel Menezes"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is home page.")

def about(request):
    return HttpResponse("This is about page.")

def services(request):
    return HttpResponse("This is services page.")
    
def contact(request):
    if request.method == "POST":
        print("form is submitted!")
        name = request.POST.get('name')

        # print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        print(name, email, phone, description)

        contact = Contact(name= name, email=email, phone=phone, description= description, date=datetime.today())
        contact.save()


    return render(request, 'contact.html')
    
    # return HttpResponse("This is contact page.")