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
