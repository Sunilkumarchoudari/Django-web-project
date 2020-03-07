from django.shortcuts import render
from .models import aipost
from django.conf import settings

# Create your views here.
def home(request):
    context = {
        'title':'HowItWorks - Home',
        'welcome_messages':['Hello,Welcome',"I'm PC"],
    }
    return render(request,'main/home.html',context=context)


def ai(request):
    ai_posts = aipost.objects.all()
    context = {
        'title':'HowItWorks - AI Projects',
        'welcome_messages':['ML/DL/AI Projects'],
        'posts':ai_posts,
    }
    return render(request,'main/ai.html',context=context)

def robotics(request):
    context = {
        'title':'HowItWorks - Robotics Projects',
        'welcome_messages':['Robotics Projects'],
    }
    return render(request,'main/robotics.html',context=context)

def physics(request):
    context = {
        'title':'HowItWorks - Physics',
        'welcome_messages':['Physics'],
    }
    return render(request,'main/physics.html',context=context)

def contact(request):
    context = {
        'title':'HowItWorks - Contact Me',
        'welcome_messages':['Contact Me'],
    }
    return render(request,'main/contact.html',context=context)

def handler404(request,exception):
    context = {
        'title':"Not Found...",
        'welcome_messages':["404!!!","Not Found"]
    }
    return render(request,'main/404.html',context = context)

def site_status(request):
    context = {
        'title':"Site Status",
        'welcome_messages':["Site Status"],
        'models_loaded': settings.MODELS.values(),
    }
    return render(request,'main/site_status.html',context=context)