from django.shortcuts import render

# Create your views here.
def renderHome(request):
    return render(request, 'home.html')