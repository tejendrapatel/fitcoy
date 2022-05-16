from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zfitcoy.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, message
from fitcoy.settings import EMAIL_HOST_USER
from fitcoy.settings import RAZORPAY_KEY_ID
from fitcoy.settings import RAZORPAY_ACCESS_KEY
from django.contrib.auth.models import User
import json
import razorpay
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_ACCESS_KEY))


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
    blo = Blogs.objects.all()
    blog= blo[:3]
    d = {"ser":ser,"blog":blog}
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
    comc = Comments.objects.all()
    com = comc[:10]
    if request.method == "POST":
        c = request.POST
        cname = c['nam']
        clname = c['mai']
        imgg = request.FILES['img']
        cmessage = c['com']
        Comments.objects.create(name=cname,email=clname,image=imgg,message=cmessage)
        return redirect('blogs')
    d = {"blosingle":blosingle,"ca":ca,"p":p,"com":com}
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
        ter = MCQUSER.objects.filter().last()
    sersingle = Services.objects.get(id=blo_id)
    fir = Services.objects.get(id=blo_id)
    nam = fir.name
    amt = fir.price*100
   
    data={
        'amount':amt,
        'currency':'INR',
        'receipt' : 'receipt id of order',
        'notes':{ 
            "name":nam,
           
        },
    }

    order= client.order.create(data=data)
    d = {"sersingle":sersingle,"order":order}
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

def BODY_TYPES4(request):
    ter = Body_Typess.objects.get(id=4)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)

def BODY_TYPES5(request):
    ter = Body_Typess.objects.get(id=5)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)

def BODY_TYPES6(request):
    ter = Body_Typess.objects.get(id=6)
    d = {"ter": ter}
    return render(request, 'pages/body_types.html',d)

def QUIZ_USER(request):
    if request.method == "POST":
        c = request.POST
        cname = c['ema']
        cmob = c['mob']
        cage = c['nam']
        MCQUSER.objects.create(name=cage, email=cname, mobile=cmob)
        return redirect('mcqs')
    count_quctions = MCQQUCTIONS.objects.all()
    d={'count_quctions':count_quctions, 'total':count_quctions.count()}
    return render(request, 'quiz_user.html',d)


def MCQS(request):
    count_quctions = MCQQUCTIONS.objects.all()
    d={'count_quctions':count_quctions, 'total':count_quctions.count()}
    return render(request, 'quiz.html',d)
 
def MCQ_ANSWER(request, blo_id):
    c = request.GET
    quctio = c['que']
    choic = c['op1']
    ter = MCQUSER.objects.filter().last()
    MCQANSWERS.objects.create(choice1=choic,quctions=quctio,categorys=ter)
    return HttpResponse(json.dumps(1), content_type="application/json")

def THANKYOU(request):
    return render(request, 'thankyou.html')



############admin ################
def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['usr']
        p = d['pass']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "admin_pannel/login.html", d)
######Used#####

def LOGOUT(request):
    logout(request)
    return redirect('home')
######Used#####

def ADMIN_CONTACT(request):
    con = Contact.objects.all()
    d = {"con": con}
    return render(request, 'admin_pannel/admin_contact.html', d)
######Used#####

def ADMIN_APPOINTMENT(request):
    con = Appionment.objects.all()
    d = {"con": con}
    return render(request, 'admin_pannel/admin_Appointment.html', d)

def ADMIN_SERVICES(request):
    if request.method == "POST":
        d = request.POST
        namm = d['nam']
        prii = d['pri']
        dell = d['det']
        aboo = d['about']
        imgg = request.FILES['img']
        Services.objects.create(name=namm, price=prii,detail=dell,discription=aboo,image=imgg)
    te = Services.objects.all()
    d = {"te":te}
    return render(request, 'admin_pannel/admin_services.html',d)

def ADMIN_BLOGS(request):
    if request.method == "POST":
        bcat = request.POST['cat']
        bhead = request.POST['nam']
        bimg = request.FILES['img']
        btxt = request.POST['txt']
        datt = request.POST['dat']

        fir = Blog_category.objects.get(name=bcat)
        fir.content = bcat
        fir.save()
        Blogs.objects.create( name=bhead, image=bimg, detail=btxt,date=datt)
    bl = Blogs.objects.all()
    d = {"bl": bl}
    return render(request, 'admin_pannel/admin_blogs.html', d)
  ##############used ##########

def ADMIN_TEAMS(request):
    if request.method == "POST":
        if 'cpma' in request.POST:
            c = request.POST
            cname = c['nam']
            postt = c['pos']
            dimg = request.FILES['img']
            face = c['fb']
            twit = c['tw']
            inst = c['in']
            link = c['li']
            deta = c['about']
            Team.objects.create(name=cname, post=postt, detail=deta, image=dimg, facebook=face, twitter=twit,instagram=inst,linkedin=link)
    camp = Team.objects.all()
    d = {"camp": camp}
    return render(request, 'admin_pannel/admin_team.html', d)
###################used#############



def ADMIN_AIR(request):
    if request.method == "POST":
            c = request.POST
            cname = c['txt']
            dimg = request.FILES['img']
            abow = Air.objects.filter(id=1)
            abow.update(image=dimg, cont=cname)
            return redirect('admin_air')
    fir = Air.objects.get(id=1)
    d = {"fir":fir}
    return render(request, 'admin_pannel/admin_air.html',d)

def ADMIN_WATER(request):
    if request.method == "POST":
            c = request.POST
            cname = c['txt']
            dimg = request.FILES['img']
            abow = Water.objects.filter(id=1)
            abow.update(image=dimg, cont=cname)
            return redirect('admin_water')
    fir = Water.objects.get(id=1)
    d = {"fir":fir}
    return render(request, 'admin_pannel/admin_water.html',d)

def ADMIN_FIRE(request):
    if request.method == "POST":
            c = request.POST
            cname = c['txt']
            dimg = request.FILES['img']
            abow = Fire.objects.filter(id=1)
            abow.update(image=dimg, cont=cname)
            return redirect('admin_fire')
    fir = Fire.objects.get(id=1)
    d = {"fir":fir}
    return render(request, 'admin_pannel/admin_fire.html',d)

def ADMIN_SPACE(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Space.objects.filter(id=1)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_space')
    fir = Space.objects.get(id=1)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_space.html',d)

def ADMIN_EARTH(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Earth.objects.filter(id=1)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_earth')
    fir = Earth.objects.get(id=1)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_earth.html',d)

def ADMIN_VAATA(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=4)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=4)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_vatta.html',d)

def ADMIN_KAPHA(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=5)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=5)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_kapha.html',d)

def ADMIN_PITTA(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=6)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=6)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_pitta.html',d)

def ADMIN_ECTOMORPH(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=1)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=1)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_ectomorph.html',d)

def ADMIN_MESOMORPH(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=2)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=2)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_mesomorph.html',d)

def ADMIN_ENDOMORPH(request):
    if request.method == "POST":
        c = request.POST
        cname = c['txt']
        dimg = request.FILES['img']
        abow = Body_Typess.objects.filter(id=3)
        abow.update(image=dimg, cont=cname)
        return redirect('admin_ectomorph')
    fir = Body_Typess.objects.get(id=3)
    d = {"fir": fir}
    return render(request, 'admin_pannel/admin_endomorph.html',d)


def ADMIN_INDEX(request):
    camd = Appionment.objects.all()
    cam = camd[:8]
    camde = Contact.objects.all()
    camh = camde[:8]
    d = {"camh":camh,"cam":cam}

    return render(request, 'admin_pannel/admin_index.html',d)








#####     admin delete ####


def ADMIN_BLOGS_DYNAMICC_DELETE(request, del_id):
    Blogs.objects.get(id=del_id).delete()
    return redirect('admin_blogs')
#######new############


def ADMIN_TEAM_DELETE(request, del_id):
    Team.objects.get(id=del_id).delete()
    return redirect('admin_Teams')

def ADMIN_SERVICE_DELETE(request, del_id):
    Services.objects.get(id=del_id).delete()
    return redirect('admin_services')

    ####  admin dynamic functions  #####


def ADMIN_BLOGS_DYNAMICC(request, bdy_id):
    blosingle = BLOGS.objects.get(id=bdy_id)
    d = {"blosingle": blosingle}
    return render(request, 'admin_blogs_dynamic.html', d)


def ADMIN_CAMPS_DYNAMICC(request, camp_id):
    if request.method == "POST":
        campna = request.POST['nam']
        nyear = request.POST['des']
        nimg = request.FILES['img']
        blosing = Camps.objects.get(id=camp_id)
        CAMPparticipants.objects.create(imag=blosing, image1=nimg, designation=nyear, name=campna)

    blosingle = Camps.objects.get(id=camp_id)
    par = CAMPparticipants.objects.filter(imag=blosingle)
    d = {"blosingle": blosingle, "par": par}
    return render(request, 'admin_camps_dynamic.html', d)

    ####  admin dynamic functions  #####

def ADMIN_BLOGS_DYNAMICC(request,bdy_id):
    blosingle = Blogs.objects.get(id=bdy_id)
    d = {"blosingle":blosingle}
    return render(request, 'admin_pannel/admin_blogs_dynamic.html',d)
###########new#########


###########Search     ######### 
def SEARCH(request):
    query = request.GET['key']
    ser = Services.objects.filter(name__icontains=query)
    d = {"ser":ser}
    return render(request,'pages/search.html',d)