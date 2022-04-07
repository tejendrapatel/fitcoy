
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
    path('privacy_policy',PRIVACY_POLICY,name='privacy_policy'),
    path('terms_conditions',TERMS_CONDITION,name='terms_conditions'),
    path('faqs',FAQSS,name='faqss'),
    path('companey_support',COMPANEYY_SUPPORTS,name='companey_support'),
    path('companey_lisence',COMPANEY_LISENCES,name='companey_lisence'),
    path('Bmi calculator',BMI,name='bmi'),
    path('Nutrition_calculator',NUTRITION_CALCULATOR,name='nutrition_calculator'),
    path('Air',AIR,name='air'),
    path('Water',WATER,name='water'),
    path('Earth',EARTH,name='earth'),
    path('Fire',FIRE,name='fire'),
    path('Space',SPACE,name='space'),
    path('Recipie',RECIPIE,name='recipie'),
    path('Ectomorph',BODY_TYPES1,name='body_types1'),
    path('Mesomorph',BODY_TYPES2,name='body_types2'),
    path('Endomorph',BODY_TYPES3,name='body_types3'),
    path('Vatta',BODY_TYPES4,name='body_types4'),
    path('Kapha',BODY_TYPES5,name='body_types5'),
    path('Pitta',BODY_TYPES6,name='body_types6'),
    path('Quiz',MCQS, name='mcqs'),
    path('UserVerification',QUIZ_USER, name='quiz_user'),
    path('Thankyou',THANKYOU, name='thankyou'),

    ####           dynamic urls       #######
    path('Quiz/<int:blo_id>/',MCQ_ANSWER, name='mcq_answer'),
    path('Blogs/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
    path('Blog/<int:blo_id>/',BLOG_CATEGORY_FILTER, name='blog_category_filter'),
    path('Service/<int:blo_id>/',SERVICES_SINGLE, name='services_single'),
    path('Team/<int:blo_id>/',TEAM_SINGLE, name='team_single'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
