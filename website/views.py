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

def project(request, context={}):
    context['title'] = "Oregon Convention Center"
    return render(request, 'project.html', context)

def services(request, context={}):
    context['title'] = "Services"
    return render(request, 'services.html', context)

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Modernized Power Utility Training"
    context['subtitle'] = "Learning Management System"
    return render(request, 'work/case-studies/nwpp.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "Enterprise CMS for the Global Ethics Leader"
    context['subtitle'] = ""
    return render(request, 'work/case-studies/navex.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Engaging the Next Generation of Scientists, Engineers, and Artists"
    context['subtitle'] = "Class Registration System"
    return render(request, 'work/case-studies/sa.html', context)

def contact(request, context={}):
    context['title'] = "Contact"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Careers"
    return render(request, 'careers.html', context)
