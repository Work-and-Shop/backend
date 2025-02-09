from rest_framework import generics
from .models import *
from .serializers import *
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    authentication_classes = []
    permission_classes = []


class UserContactCreateView(generics.CreateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    authentication_classes = []
    permission_classes = []

    def perform_create(self, serializer):
        user = serializer.save()

        # Email Content
        subject = "Download the Work and Shop App!"
        message = f"Hello {user.full_name},\n\nThank you for signing up! 🎉\n\nDownload our app from the Play Store:\nhttps://play.google.com/store/apps/details?id=com.workandshop\n\nBest regards,\nWork and Shop Team"
        sender = settings.EMAIL_HOST_USER
        recipient = [user.email]

        send_mail(subject, message, sender, recipient, fail_silently=False)

        return Response({"message": "User registered successfully! Email sent."})