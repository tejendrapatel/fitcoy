
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
    path('recipe',RECIPE,name='recipe'),
    path('team',TEAMS,name='team'),
    path('privacy_policy',PRIVACY_POLICY,name='privacy_policy'),
    path('terms_conditions',TERMS_CONDITION,name='terms_conditions'),
    path('faqss',FAQSS,name='faqss'),
    path('companey_support',COMPANEYY_SUPPORTS,name='companey_support'),
    path('companey_lisence',COMPANEY_LISENCES,name='companey_lisence'),
    path('bmi',BMI,name='bmi'),
    path('nutrition_calculator',NUTRITION_CALCULATOR,name='nutrition_calculator'),
    path('air',AIR,name='air'),
    path('water',WATER,name='water'),
    path('earth',EARTH,name='earth'),
    path('fire',FIRE,name='fire'),
    path('space',SPACE,name='space'),
    path('recipie',RECIPIE,name='recipie'),
    path('body_types1',BODY_TYPES1,name='body_types1'),
    path('body_types2',BODY_TYPES2,name='body_types2'),
    path('body_types3',BODY_TYPES3,name='body_types3'),


    ####           dynamic urls       #######
    path('mcqs/<int:blog_id>/',MCQS, name='mcqs'),
    path('blog_single/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
    path('blog_category_filter/<int:blo_id>/',BLOG_CATEGORY_FILTER, name='blog_category_filter'),
    path('services_single/<int:blo_id>/',SERVICES_SINGLE, name='services_single'),
    path('team_single/<int:blo_id>/',TEAM_SINGLE, name='team_single'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
