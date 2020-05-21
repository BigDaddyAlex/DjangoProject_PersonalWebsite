from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name = 'home.html'

class aboutPageView(TemplateView):
    template_name = 'about.html'

class contactPageView(TemplateView):
    template_name = 'contact.html'