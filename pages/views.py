from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactUsView(TemplateView):
    template_name = 'contactus.html'