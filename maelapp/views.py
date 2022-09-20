from django.shortcuts import render
from maelapp.forms import FeedbackForm
from maelapp.models import Portfolio, UploadImage

siteTitle = "Itsumi Mael!"
msgIndex = "Hey guys! I'm learning Django!"
msgPortfolio = "A list of my most recent projects."
msgContactUs = "Let's connect!"

def index(request):
    frontImages = UploadImage.objects.all()
    context = {'siteTitle':siteTitle,'pageTitle':'Itsumi Mael!','text':msgIndex, 'frontImage':frontImages}
    return render(request, "base_content.html", context)

def portfolio(request):
    # get all records from Portfolio model
    porfolioData = Portfolio.objects.all().order_by('-endDate') # descending order by id
    context = {'siteTitle':siteTitle,'pageTitle':'Portfolio','text':msgPortfolio,'data':porfolioData} 
    return render(request, "base_content.html", context)

def contact(request):
    context = {'siteTitle':siteTitle,'pageTitle':'Contact Me','text':msgContactUs} # establish basic context
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just triggers the validation
            form.save()
            form = FeedbackForm()
            context.update({'form':form.as_table, 'created':True}) # update basic context
            return render(request, "base_content.html", context)
        else:
            context.update({'form':form.as_table, 'notcreated':True}) # update basic context
            return render(request, "base_content.html", context)
    else:
        form = FeedbackForm()
    context.update({'form':form.as_table}) # update basic context
    return render(request, "base_content.html", context)