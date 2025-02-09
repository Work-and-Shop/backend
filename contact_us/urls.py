from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactUsCreateView.as_view(), name='contact-us'),
    path('/inquire', UserContactCreateView.as_view(), name='user-register'),
]
