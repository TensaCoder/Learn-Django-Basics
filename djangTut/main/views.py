from django.shortcuts import render, HttpResponse

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
    
    return render(request, 'contact.html')
    
    # return HttpResponse("This is contact page.")