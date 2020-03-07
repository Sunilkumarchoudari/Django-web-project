from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home_page'),
    path('ai',views.ai,name = 'ai_page'),
    path('physics',views.physics, name = 'physics_page'),
    path('robotics',views.robotics, name = 'robotics_page'),
    path('contact',views.contact,name='contact_page'),
    path('status',views.site_status,name='site_status_page'),
]