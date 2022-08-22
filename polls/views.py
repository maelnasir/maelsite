from django.http import HttpResponse

user = "Ismail"
def index(request):
    return HttpResponse("Hello, " + user + ". You're at the polls index.");