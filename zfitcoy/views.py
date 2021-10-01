from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zfitcoy.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, message
from fitcoy.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

def HOME(request):
    if request.method == "POST":
        c = request.POST
        cname = c['name']
        clname = c['date']
        ctime = c['time']
        cmobile = c['phone']
        cmessage = c['message']
        Appionment.objects.create(name=cname,date=clname,mobile=cmobile,time=ctime,message=cmessage)
        return redirect('home')
    ser = Services.objects.all()
    d = {"ser":ser}
    return render(request, 'pages/index.html',d)

def ABOUT(request):
    return render(request, 'pages/about.html')

def RECIPE(request):

    return render(request, 'pages/about.html')

def SERVICES(request):
    ser = Services.objects.all()
    d = {"ser":ser}
    return render(request, 'pages/service.html',d)

def BLOGS(request):
    pop = Blog_category.objects.get(id=3)
    blog = Blogs.objects.filter(categorys=pop)
    p = blog[:3]
    d = {"blog":blog,"p":p}
    return render(request, 'pages/blogs.html',d)


def RECIPIE(request):
    pop = Blog_category.objects.get(id=4)
    rec = Blogs.objects.filter(categorys=pop)
    p = rec[:3]
    d = {"rec":rec,"p":p}
    return render(request, 'pages/recipie.html',d)



def CONTACT(request):
    if request.method == "POST":
        c = request.POST
        cname = c['name']
        clname = c['subject']
        cemail = c['email']
        cmobile = c['phone']
        cmessage = c['message']

        email = 'fit.indcoy@@gmail.com'
        subject = "Contact US Requests "
        content = "Fitcoy"
        Contact.objects.create(name=cname, email=cemail, mobile=cmobile, query=clname,message=cmessage)
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'cname': cname, 'clname': clname, "cemail": cemail, "cmobile": cmobile, "cmessage": cmessage}
        html = get_template('email3.html').render(d)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        return redirect('contact')
    return render(request, 'pages/contact.html')

def TEAMS(request):
    te = Team.objects.all()
    d = {"te":te}
    return render(request, 'pages/team.html',d)



# def MCQS(request):
#     if request.method == "POST":
#         fnam = request.POST['fnam']
#         llname = request.POST['lnam']
#         emai = request.POST['emil']
#         mmob = request.POST['mob']
#         uu = MCQUSER.objects.create(fname=fnam,lname=llname,email=emai,mobile=mmob)
#         for i in li:
#             cname = request.POST['cho' + str(i)]
#             que = request.POST['quu' + str(i)]
#             MCQANSWERS.objects.create(choice1=cname,quctions=que,categorys=uu)
#         return redirect('home')
#     d = {}
#     return render(request, 'quiz2.html',d) 

#########dynamic pages ##################

def BLOG_CATEGORY_FILTER(request,blo_id):
    cat = Blog_category.objects.get(id=blo_id)
    blog = Blogs.objects.filter(categorys=cat)
    pop = Blogs.objects.all().order_by('id')
    p = pop[:3]
    ca = Blog_category.objects.all()
    blog = Blogs.objects.all()
    d = {"blog":blog,"blog":blog,"ca":ca,"p":p}
    return render(request, 'dynamic/blogs_category_filter.html',d)


def BLOG_SINGLE(request,blo_id):
    blosingle = Blogs.objects.get(id=blo_id)
    pop = Blogs.objects.all().order_by('id')
    p = pop[:3]
    ca = Blog_category.objects.all()
    
    d = {"blosingle":blosingle,"ca":ca,"p":p}
    return render(request, 'dynamic/blog-single.html',d)

def SERVICES_SINGLE(request,blo_id):
    if request.method == "POST":
        c = request.POST
        cname = c['name']
        cmob = c['mobile']
        cage = c['Age']
        cmail = c['mail']
        cmessage = c['message']
        SERVICE_CONTACT.objects.create(name=cname, email=cmail, mobile=cmob, age=cage,message=cmessage)
    sersingle = Services.objects.get(id=blo_id)
    d = {"sersingle":sersingle}
    return render(request, 'dynamic/services_single.html',d)

def TEAM_SINGLE(request,blo_id):
    sersingle = Team.objects.get(id=blo_id)
    d = {"sersingle":sersingle}
    return render(request, 'dynamic/team_single.html',d)


###########policies#######
def PRIVACY_POLICY(request):
    ter = PRIVACY_POLICYs.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/privacy_policy.html',d)

def TERMS_CONDITION(request):
    ter = TERMS_CONDITIONSs.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/terms_conditions.html',d)

def FAQSS(request):
    fa = faqss.objects.all()
    d = {"fa": fa}
    return render(request, 'admin/faqss.html',d)

def COMPANEYY_SUPPORTS(request):
    ter = COMPANEY_SUPPORTS.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/companey_support.html',d)

def COMPANEY_LISENCES(request):
    ter = WHY_CHOOSE_Us.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/companey_lisence.html',d)

def BMI(request):
    
    return render(request, 'pages/BMI_calculator.html')

def NUTRITION_CALCULATOR(request):
    
    return render(request, 'pages/Nutrition_calculator.html')

def SPACE(request):
    ter = Space.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/space.html',d)

def FIRE(request):
    ter = Fire.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/fire.html',d)

def EARTH(request):
    ter = Earth.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/earth.html',d)

def WATER(request):
    ter = Water.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/water.html',d)

def AIR(request):
    ter = Air.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'admin/air.html',d)

def BODY_TYPES1(request):
    ter = Body_Typess.objects.get(id=1)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)

def BODY_TYPES2(request):
    ter = Body_Typess.objects.get(id=2)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)

def BODY_TYPES3(request):
    ter = Body_Typess.objects.get(id=3)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)


z=0
def MCQS(request,blog_id):
    if request.method == "POST":
        c = request.POST
        name1 = c['op1']
        MCQANSWERS.objects.create(choice1=name1)
    cat = MCQQUCTIONS.objects.get(id=blog_id)
    count_quctions = MCQQUCTIONS.objects.all()
    li =  []
    count=0
    for i in count_quctions:
        li.append(i.id)
        count += 1
    global z 
    if z<count:
        z=z+1  
        return render(request, 'index.html',{'z':z,'cat':cat})
    elif z==17:
        z = 0
        return redirect('about')
    else: 
        z=0
        return redirect('about')