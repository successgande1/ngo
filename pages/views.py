from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

#About Page View
def about(request):
    return render(request, 'pages/about.html')

