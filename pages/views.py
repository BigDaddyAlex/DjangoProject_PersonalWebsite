from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Contactform, Topicform
from .models import ContactMsg, Topic
import inspect
from django.core.mail import send_mail
from django.utils.timezone import datetime

def homeView(request): 
    alltopics=Topic.objects.all()
    topics=alltopics.values()
    topic=topics
    print(topics)
    return render(request, "home.html",{'topics':topics})

class aboutPageView(TemplateView):
    template_name = 'about.html'

class thanksPageView(TemplateView):
    template_name = 'thanks.html'

class projectsPageView(TemplateView):
    template_name = 'projects.html'
 
def get_msg(request):
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            femail=form.cleaned_data['femail']
            fmsg=form.cleaned_data['fmessage']
            s= ContactMsg(contact_name=fname,contact_email=femail,contact_msg=fmsg)
            s.save()
        return redirect('/contact/thanks/')
    else:
        form=Contactform()
    return render(request,'contact.html',{'form':form})

def get_topic(request):
    if request.method=='POST':
        form=Topicform(request.POST)
        if form.is_valid():
            topic_name=form.cleaned_data['topic_name']
            topic_TLDR=form.cleaned_data['topic_TLDR']
            topic_body=form.cleaned_data['topic_body']
            topic_last_modified = datetime.now()
            s=Topic(topic_name=topic_name,topic_TLDR=topic_TLDR,topic_body=topic_body,topic_last_modified=topic_last_modified)
            s.save()
        return redirect('/addtopic')
    else:
        form=Topicform()
    return render(request,'addtopic.html',{'form':form})