from django.shortcuts import render

def home(request, context={}):
    context['title'] = "OMBU Website homepage"
    return render(request, 'home.html', context)