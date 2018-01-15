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

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    return render(request, 'careers.html', context)

# Work / Case Studies
# ##############################################################################

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
    context['banner_image'] = "website/images/case-studies/nwpp/banner.png"
    context['banner_title'] = "Modernized Power Utility Training"
    context['banner_subtitle']  = "Learning Management System"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Northwest PowerPool (NWPP)</span> brings together 32 power utilities in eight US states and two Canadian provinces. OMBU designed a powerful centralized training platform so NWPP could help its member utilities keep up-to-date on mandated certifications and the latest trends, meaning greater safety, more engagement, and more benefit to the whole membership base and their customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/nwpp/testimonial-logo.png"
    context['testimonial_quote'] = "“Partnering with OMBU on this evolution of our platform was one of the best decisions I’ve ever made.”"
    context['testimonial_attribution_name'] = "David Pennington"
    context['testimonial_attribution_title'] = "Curriculum Developer, NWPP"
    context['contribution_skills'] = ["User Experience Design", "Python Application Development", "AWS Infrastructure", "Product Roadmap Planning"]
    return render(request, 'work/case-studies/nwpp.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "Case study for NAVEX Global’s enterprise CMS"
    context['banner_image'] = "website/images/case-studies/navex/banner.png"
    context['banner_title'] = "Enterprise CMS for the Global Ethics Leader"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">NAVEX Global</span> was formed in 2012 to become the leader in the emerging field of Ethics & Compliance. They engaged OMBU with the mission to design and launch technology capable of not just keeping up, but accelerating, their meteoric rise.</p>"
    context['testimonial_image'] = "website/images/case-studies/navex/testimonial-logo.png"
    context['intro_testimonial_quote'] = "“Based on projects, the current uplift in high-value forms from the new pages will result in $4.6M in pipe and $1.4M in closed won business in the next 12 months!”"
    context['intro_testimonial_attribution_name'] = "Hillary Ervin"
    context['intro_testimonial_attribution_title'] = "Senior Director, Demand Generation & Sales Development Team"
    context['contribution_skills'] = ["Technology Strategy", "Enterprise CMS", "Drupal CMS Development", "Marketo Integration", "AWS Migration", "AWS Infrastructure Management"]
    return render(request, 'work/case-studies/navex.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Case study for Saturday Academy’s class registration system"
    context['banner_image'] = "website/images/case-studies/sa/banner.png"
    context['banner_title'] = "Engaging the Next Generation of Scientists, Engineers, and Artists"
    context['banner_subtitle'] = "Class Registration System"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Saturday Academy</span> strives to engage all motivated young people in hands-on, in-depth learning by connecting them to community experts as educators and mentors by offering over 850 STEAM-curriculum classes per year. But registration was cumbersome for parents and data collection was poor and incomplete.</p><p>  OMBU conducted an organization-wide survey of processes, workflows and technology usage and designed and built a nonprofit Salesforce CRM and integrated website that enables families to register to classes and engage with mentors, funneling data in real time into Salesforce for instant reporting and analysis. This IT revision transformed how Saturday Academy engages with its customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/sa/testimonial-logo.png"
    context['contribution_skills'] = ["Technology Strategy", "User Experience Design", "Visual Design", "Salesforce CRM Development", "Drupal Application Development", "AWS Design & Implementation"]
    return render(request, 'work/case-studies/sa.html', context)
