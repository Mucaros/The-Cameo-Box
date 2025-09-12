from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactSubmission
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt  # remove this later for security
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        ContactSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Send email
        send_mail(
            subject=f"New Contact Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['your-email@example.com'],  # <- replace with your email
        )

        return HttpResponse("Thanks for your message!")

    return HttpResponse("Only POST requests are allowed.")