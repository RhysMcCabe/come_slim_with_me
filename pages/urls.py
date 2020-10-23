from django.urls import path
from .views import HomePageView, ContactUsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contactus/', ContactUsView.as_view(), name='contactus'),
]