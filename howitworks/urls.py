from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main_urls
from ai import urls as ai_urls
from about import views as about_views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main_urls)),
    path('about/',about_views.about,name='about_page'),
    path('ai/',include(ai_urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler404'