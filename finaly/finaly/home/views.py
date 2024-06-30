from django.shortcuts import render
from .models import Treners, News, Contact
from django.core.mail import send_mail


# Create your views here.
def home(request):
    treners = Treners.objects.all()
    news = News.objects.all()
    context = {
        'treners': treners,
        'news': news,
    }
    return render(
        request=request,
        template_name='index.html',
        context=context
    )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('message')
        number = request.POST.get('number')
        contact_us = Contact(email=email, name=name, message=message, number=number)
        contact_us.save()
    
    return render(
        request=request,
        template_name='contact.html',
    )


def treiner(request):
    treners = Treners.objects.all()
    context = {
        'treners': treners
    }
    return render(
        request=request,
        template_name='trainer.html',
        context=context
    )
