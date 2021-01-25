from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"This is sent"
    }
    return render(request,'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")
