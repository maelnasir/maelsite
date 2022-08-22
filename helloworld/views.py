from django.shortcuts import render
from helloworld.forms import FeedbackForm
from helloworld.models import Portfolio

msgIndex = "Hello World! I'm learning Django!";
msgPortfolio = "A list of my most recent projects.";
msgContactUs = "Let's connect!";

def index(request):
    context = {'title':'Hello World!','text':msgIndex}
    return render(request, "base.html", context);

def portfolio(request):
    # get all records from Portfolio model
    porfolioData = Portfolio.objects.all()
    context = {'title':'Portfolio','text':msgPortfolio,'data':porfolioData} 
    return render(request, "base.html", context);

def contact(request):
    context = {'title':'Contact Me', 'text':msgContactUs}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
            form.save()
            form = FeedbackForm()
            context.update({'form':form.as_table, 'created':True}) # add to context
            return render(request, "base.html", context);
        else:
            context.update({'form':form.as_table, 'notcreated':True}) # add to context
            return render(request, "base.html", context);
    else:
        form = FeedbackForm()
    context.update({'form':form.as_table}) # add to context
    return render(request, "base.html", context);