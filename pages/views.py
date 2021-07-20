from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

#About Page View
def about(request):
    return render(request, 'pages/about.html')

#Contact Page View
def contact(request):
    return render(request, 'pages/contact.html')

#FAQ Page View
def faq(request):
    return render(request, 'pages/faq.html')

#Programs Page View
def programs(request):
    return render(request, 'pages/programs.html')


