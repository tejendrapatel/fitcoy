
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
    path('thankyou',THANKYOU, name='thankyou'),

    ####           dynamic urls       #######
    path('Quiz/<int:blo_id>/',MCQ_ANSWER, name='mcq_answer'),
    path('Blogs/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
    path('Blog/<int:blo_id>/',BLOG_CATEGORY_FILTER, name='blog_category_filter'),
    path('Service/<int:blo_id>/',SERVICES_SINGLE, name='services_single'),
    path('Team/<int:blo_id>/',TEAM_SINGLE, name='team_single'),
#####       admin pannel   ##########

    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    path('admin_index',ADMIN_INDEX,name= 'admin_index'),
    path('admin_contact',ADMIN_CONTACT,name= 'admin_contact'),
    path('admin_appointment', ADMIN_APPOINTMENT, name='admin_appointment'),
    path('admin_blogs', ADMIN_BLOGS, name='admin_blogs'),
    path('admin_Teams', ADMIN_TEAMS, name='admin_Teams'),
    path('admin_services', ADMIN_SERVICES, name='admin_services'),
    path('admin_air',ADMIN_AIR,name= 'admin_air'),
    path('admin_water',ADMIN_WATER,name= 'admin_water'),
    path('admin_fire',ADMIN_FIRE,name= 'admin_fire'),
    path('admin_space',ADMIN_SPACE,name= 'admin_space'),
    path('admin_earth',ADMIN_EARTH,name= 'admin_earth'),
    path('admin_vaata',ADMIN_VAATA,name= 'admin_vatta'),
    path('admin_kapha',ADMIN_KAPHA,name= 'admin_kapha'),
    path('admin_pitta',ADMIN_PITTA,name= 'admin_pitta'),
    path('admin_ectomorph',ADMIN_ECTOMORPH,name= 'admin_ectomorph'),
    path('admin_mesomorph',ADMIN_MESOMORPH,name= 'admin_mesomorph'),
    path('admin_endomorph',ADMIN_ENDOMORPH,name= 'admin_endomorph'),



####### admin dynamic functions  ######
    path('admin_blogs_dynamic/<int:bdy_id>/', ADMIN_BLOGS_DYNAMICC, name='admin_blogs_dynamic'),

##############admin delete ###########
    path('admin_blogs_delete/<int:del_id>/', ADMIN_BLOGS_DYNAMICC_DELETE, name='admin_blogs_delete'),
    path('admin_team_delete/<int:del_id>/', ADMIN_TEAM_DELETE, name='admin_team_delete'),
path('admin_service_delete/<int:del_id>/', ADMIN_SERVICE_DELETE, name='admin_service_delete'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
