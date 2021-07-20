from django.urls import path
#import the views module
from . import views

#Create url patterns
urlpatterns = [
    path('', views.index, name = 'pages-index'),
    path('about', views.about, name = 'pages-about'),
    path('contact', views.contact, name = 'pages-contact'),
    path('faq', views.faq, name = 'pages-faq'),
    path('programs', views.programs, name = 'pages-programs'),
]