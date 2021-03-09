from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, message, subject)

        email = EmailMessage(
            'Message from ' + name,
            message + "\n" + email,
            settings.EMAIL_HOST_USER,
            ['rahulsaraf1578@gmail.com'],
        )
        fail_silently = False
        email.send()

        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'index.html', {})

# Django administration
# rahulsaraf

