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

# Experimental
# ------------------------------------------------------------------------------

def exp_index(request, context={}):
    context['title'] = "Experiments"
    return render(request, 'experimental/index.html', context)

def exp_transitions(request, context={}):
    context['title'] = "Experimental — Page Transitions"
    return render(request, 'experimental/transitions/index.html', context)

def exp_transitions_a_rock(request, context={}):
    context['title'] = "Experimental — Page Transitions A — Rock"
    return render(request, 'experimental/transitions/a/rock.html', context)

def exp_transitions_a_paper(request, context={}):
    context['title'] = "Experimental — Page Transitions A — Paper"
    return render(request, 'experimental/transitions/a/paper.html', context)

def exp_transitions_a_scissors(request, context={}):
    context['title'] = "Experimental — Page Transitions A — Scissors"
    return render(request, 'experimental/transitions/a/scissors.html', context)

def exp_transitions_b_rock(request, context={}):
    context['title'] = "Experimental — Page Transitions B — Rock"
    return render(request, 'experimental/transitions/b/rock.html', context)

def exp_transitions_b_paper(request, context={}):
    context['title'] = "Experimental — Page Transitions B — Paper"
    return render(request, 'experimental/transitions/b/paper.html', context)

def exp_transitions_b_scissors(request, context={}):
    context['title'] = "Experimental — Page Transitions B — Scissors"
    return render(request, 'experimental/transitions/b/scissors.html', context)

def exp_rings(request, context={}):
    context['title'] = "Experimental — Rings"
    return render(request, 'experimental/rings/index.html', context)

def exp_rings_a(request, context={}):
    context['title'] = "Experimental — Rings A"
    return render(request, 'experimental/rings/a/index.html', context)

def exp_rings_b(request, context={}):
    context['title'] = "Experimental — Rings B"
    return render(request, 'experimental/rings/b/index.html', context)

def exp_rings_c(request, context={}):
    context['title'] = "Experimental — Rings C"
    return render(request, 'experimental/rings/c/index.html', context)

def exp_rings_d(request, context={}):
    context['title'] = "Experimental — Rings D"
    return render(request, 'experimental/rings/d/index.html', context)
