from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import  *


def insert_topic(request):
    Tn=input('enter topic_name : ')
    To=Topic.objects.get_or_create(topic_name=Tn)[0]
    To.save()
    return HttpResponse("<h1>Topic name is inserted<h1/>")



def insert_webpage(request):
    Tn=input('enter topic_name : ')
    To=Topic.objects.get_or_create(topic_name=Tn)[0]
    To.save()

    n=input('Enter the name : ')
    u=input('Enter the url name : ')
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=u)[0]
    Wo.save()

    return HttpResponse("<h1>Webpage is inserted<h1/>")


def insert_acess(request):
    Tn=input('enter topic_name : ')
    To=Topic.objects.get_or_create(topic_name=Tn)[0]
    To.save()

    n=input('Enter the name : ')
    u=input('Enter the url name : ')
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=u)[0]
    Wo.save()

    Date=input('enterdate yyyy-dd-mm : ')
    Au=input('enter author name : ')
    Ao=AcessRecord.objects.get_or_create(name=Wo,date=Date,author=Au)[0]
    Ao.save()

    return HttpResponse("<h1>Acces is inserted<h1/>")






# create new views for font end

#display Topic Models

def display_topic(request):
    topics=Topic.objects.filter(topic_name='Footbal')
    d={'topics':topics}
    return render(request,'display_topic.html',d)

#display Webpage Models

def display_webpage(request):
    webpages=Webpage.objects.filter(topic_name='Footbal')
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

#display AccessRecord Models

def display_AcessRecord(request):
    Acess=AcessRecord.objects.all()
    d={'Acess':Acess}
    return render(request,'display_AcessRecord.html',d)

