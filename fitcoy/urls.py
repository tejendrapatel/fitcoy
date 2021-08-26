
from django.contrib import admin
from django.urls import path
from zfitcoy.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
urlpatterns = [
     path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',HOME,name= 'home'),
    path('about',ABOUT,name= 'about'),
    path('services',SERVICES,name='services'),
    path('blogs',BLOGS,name='blogs'),
    path('contact',CONTACT,name='contact'),
    path('team',TEAMS,name='team'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
