from django.shortcuts import render

def home(request, context={}):
    context['title'] = "OMBU Website homepage"
    return render(request, 'home.html', context)

def about(request, context={}):
    context['title'] = "About OMBU Website homepage"
    return render(request, 'about.html', context)

def kitchensink(request, context={}):
    context['title'] = "Kitchen Sink"
    return render(request, 'kitchen_sink.html', context)    

def work(request, context={}):
    context['title'] = "Work"
    return render(request, 'work.html', context)