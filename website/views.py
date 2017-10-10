from django.shortcuts import render

def home(request, context={}):
    context['title'] = "OMBU Website homepage"
    return render(request, 'home.html', context)

def about(request, context={}):
    context['title'] = "About OMBU Website homepage"
    return render(request, 'about.html', context)


# Experimental
# ------------------------------------------------------------------------------

def exp_transitions_rock(request, context={}):
    context['title'] = "Experimental — Page Transitions — Rock"
    return render(request, 'experimental/transitions/rock.html', context)

def exp_transitions_paper(request, context={}):
    context['title'] = "Experimental — Page Transitions — Paper"
    return render(request, 'experimental/transitions/paper.html', context)

def exp_transitions_scissors(request, context={}):
    context['title'] = "Experimental — Page Transitions — Scissors"
    return render(request, 'experimental/transitions/scissors.html', context)
