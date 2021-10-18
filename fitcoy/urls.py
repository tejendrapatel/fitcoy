
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
    path('Body_types',BODY_TYPES1,name='body_types1'),
    path('Body_types',BODY_TYPES2,name='body_types2'),
    path('Body_types',BODY_TYPES3,name='body_types3'),
    path('Quiz',MCQS, name='mcqs'),
    path('Quiz',QUIZ_USER, name='quiz_user'),
    path('Quiz',THANKYOU, name='thankyou'),

    ####           dynamic urls       #######
    path('Quiz/<int:blo_id>/',MCQ_ANSWER, name='mcq_answer'),
    path('Blogs/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
    path('Blog/<int:blo_id>/',BLOG_CATEGORY_FILTER, name='blog_category_filter'),
    path('Service/<int:blo_id>/',SERVICES_SINGLE, name='services_single'),
    path('Team/<int:blo_id>/',TEAM_SINGLE, name='team_single'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
