from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Contactform
from .models import ContactMsg
import inspect
from django.core.mail import send_mail

class homePageView(TemplateView):
    template_name = 'home.html'

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

            
            # fmessage='From: '+fname+'\n'+'Email: '+femail+'\n'+form.cleaned_data['fmessage']
            # recipients=['sqcalexander@gmail.com']
            # subject='New Msg from Django App'
            # send_mail(subject,fmessage,femail,recipients)
        return redirect('/contact/thanks/')
    else:
        form=Contactform()
    return render(request,'contact.html',{'form':form})

