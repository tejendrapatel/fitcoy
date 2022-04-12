
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
#####       admin pannel   ##########

    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    path('Forgot/',FORGOT,name='Forgot'),
    path('admin_index',ADMIN_INDEX,name= 'admin_index'),
    path('admin_contact',ADMIN_CONTACT,name= 'admin_contact'),
    path('admin_opportunities',ADMIN_OPPORTUNITIES,name= 'admin_opportunities'),
    path('admin_mail',ADMIN_MAIl,name= 'admin_mail'),
    path('admin_about',ADMIN_ABOUT,name= 'admin_about'),
    path('admin_home', ADMIN_HOME, name='admin_home'),
    path('admin_home2', ADMIN_HOME2, name='admin_home2'),
    path('admin_home3', ADMIN_HOME3, name='admin_home3'),
    path('admin_home4', ADMIN_HOME4, name='admin_home4'),
    path('admin_camps', ADMIN_CAMPS, name='admin_camps'),
    path('admin_news', ADMIN_NEWS, name='admin_news'),
    path('admin_gallery', ADMIN_GALLERY, name='admin_gallery'),
    path('admin_blogs', ADMIN_BLOGS, name='admin_blogs'),
    path('admin_events', ADMIN_EVENTS, name='admin_events'),
    path('admin_youtube',ADMIN_YOUTUBE, name='admin_youtube'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
