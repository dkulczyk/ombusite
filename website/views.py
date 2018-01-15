from django.shortcuts import render

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, infrastructure, and tech strategy"
    return render(request, 'home.html', context)

def about(request, context={}):
    context['title'] = "The web technology agency for visionaries"
    return render(request, 'about.html', context)

def kitchensink(request, context={}):
    context['title'] = "Kitchen Sink"
    return render(request, 'kitchen_sink.html', context)

def work(request, context={}):
    context['title'] = "Case studies and project profiles for our web technology solutions"
    return render(request, 'work.html', context)

def project(request, context={}):
    context['title'] = "Oregon Convention Center"
    return render(request, 'project.html', context)

def services(request, context={}):
    context['title'] = "Enterprise CMS, business applications, infrastructure, and technology strategy"
    return render(request, 'services.html', context)

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
    context['subtitle'] = "Learning Management System"
    context['contribution_skills'] = ["User Experience Design", "Python Application Development", "AWS Infrastructure", "Product Roadmap Planning"]
    return render(request, 'work/case-studies/nwpp.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "Case study for NAVEX Global’s enterprise CMS"
    context['subtitle'] = ""
    context['contribution_skills'] = ["Technology Strategy", "Enterprise CMS", "Drupal CMS Development", "Marketo Integration", "AWS Migration", "AWS Infrastructure Management"]
    return render(request, 'work/case-studies/navex.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Case study for Saturday Academy’s class registration system"
    context['subtitle'] = "Class Registration System"
    context['contribution_skills'] = ["Technology Strategy", "User Experience Design", "Visual Design", "Salesforce CRM Development", "Drupal Application Development", "AWS Design & Implementation"]
    return render(request, 'work/case-studies/sa.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    return render(request, 'careers.html', context)
