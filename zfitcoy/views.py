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
        ter = MCQUSER.objects.filter().last()
    sersingle = Services.objects.get(id=blo_id)
    data={
        'amount' : 100*100,
        'currency' : 'INR',
        'receipt' : 'receipt id of order',
        'notes':{ 
            "name":'hgfhg',
            "service":"zumba",
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
            return redirect('admin_pannel/admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "admin_pannel/login.html", d)

def FORGOT(request):
    error = False
    form = False
    udata = False
    if request.method == "POST":
        dd = request.POST
        name = dd["form"]
        if name == "submit email":
            e = dd['em']
            user = User.objects.filter(email = e)
            if user:
                form = True
                udata = user[0]
            else:
                error = True
        if name == 'submit pwd':
            p = dd ['pwd']
            c = dd ['cpwd']
            u = dd ['idd']
            user = User.objects.get(id=u)
            user.set_password(p)
            user.save()
            return redirect ('Login')
    d = {"form":form,"error":error,"udata":udata}
    return render(request,'forgot.html',d)

def LOGOUT(request):
    logout(request)
    return redirect('home')


def ADMIN_YOUTUBE(request):
    return render(request, 'admin_youtube.html')


def ADMIN_INDEX(request):
    li = []
    em1 = EMAIL_LETTERS.objects.all()
    for i in em1:
        li.append(i.mubmail)
    if request.method == "POST":
        if 'new' in request.POST:
            c = request.POST
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            email = li
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = msg = EmailMultiAlternatives(subject, content, EMAIL_HOST_USER, email)
            d = {'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_index')
        elif 'pos' in request.POST:
            imgg = request.FILES['imagg']
            EMIMG.objects.create(imagess=imgg)
            return redirect('admin_index')
    podd = EMIMG.objects.latest('id')
    opps = Oppurtunities.objects.all().order_by('-id')
    cons = Contact.objects.all().order_by('-id')
    cam = Camps.objects.all().order_by('-id')
    opp = opps[:5]
    con = cons[:5]
    emp = Team.objects.all()
    d = {"opp": opp, "con": con, "emp": emp, "cam": cam, "podd": podd}
    return render(request, 'admin_index.html', d)


def ADMIN_CONTACT(request):
    con = Contact.objects.all()
    d = {"con": con}
    return render(request, 'admin_contact.html', d)


def ADMIN_OPPORTUNITIES(request):
    opp = Oppurtunities.objects.all()
    d = {"opp": opp}
    return render(request, 'admin_oppurtunities.html', d)


def ADMIN_MAIl(request):
    li = []
    em1 = EMAIL_LETTERS.objects.all()
    for i in em1:
        li.append(i.mubmail)
    if request.method == "POST":
        if 'em' in request.POST:
            c = request.POST
            email = c['emi']
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            d = {'email': email, 'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_mail')
        elif 'new' in request.POST:
            c = request.POST
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            email = li
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = msg = EmailMultiAlternatives(subject, content, EMAIL_HOST_USER, email)
            d = {'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_mail')

    return render(request, 'admin_mail.html')


def ADMIN_ABOUT(request):
    abo = About.objects.get(id=1)
    abo2 = About.objects.get(id=2)
    abo3 = About.objects.get(id=3)
    emp = Team.objects.all()
    if request.method == "POST":
        if 'about' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=1)
            abow.update(heading=hedd, paragraph=parr, image1=imgg)
            return redirect('admin_about')
        elif 'history' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=2)
            abow.update(heading=hedd, paragraph=parr, image1=imgg)
            return redirect('admin_about')
        elif 'objective' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=3)
            abow.update(heading=hedd, paragraph=parr, image1=imgg)
            return redirect('admin_about')
        elif 'team' in request.POST:
            c = request.POST
            nam = c['head']
            mobi = c['mob']
            imgg = request.FILES['img']
            idobbb = c['dobb']
            emaill = c['emai']
            desi = c['desig']
            Team.objects.create(name=nam, mobile=mobi, image1=imgg, dob=idobbb, email=emaill, designation=desi)
            return redirect('admin_about')
    d = {"emp": emp, "abo": abo, "abo2": abo2, "abo3": abo3}
    return render(request, 'admin_about.html', d)


def ADMIN_HOME(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam, position=posit, image=imgg, Detail=detai, facebook=face,
                                     linkedin=linkedi, instagram=insta, twitter=twitt)
            return redirect('admin_home')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_ABOUT.objects.filter(id=1)
            bans.update(Discription=posit)
            return redirect('admin_home')
    test = TESTIMONY.objects.all()
    ban = BANNER_ABOUT.objects.get(id=1)
    d = {"test": test, "ban": ban}
    return render(request, 'admin_home.html', d)


def ADMIN_HOME2(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam, position=posit, image=imgg, Detail=detai, facebook=face,
                                     linkedin=linkedi, instagram=insta, twitter=twitt)
            return redirect('admin_home2')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_CAMPS.objects.filter(id=1)
            bans.update(Discription=posit)
            return redirect('admin_home2')
    test = TESTIMONY.objects.all()
    ban = BANNER_CAMPS.objects.get(id=1)
    d = {"test": test, "ban": ban}
    return render(request, 'admin_home2.html', d)


def ADMIN_HOME3(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam, position=posit, image=imgg, Detail=detai, facebook=face,
                                     linkedin=linkedi, instagram=insta, twitter=twitt)
            return redirect('admin_home3')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_ANANTMANDI.objects.filter(id=1)
            bans.update(Discription=posit)
            return redirect('admin_home3')
    test = TESTIMONY.objects.all()
    ban = BANNER_ANANTMANDI.objects.get(id=1)
    d = {"test": test, "ban": ban}
    return render(request, 'admin_home3.html', d)


def ADMIN_HOME4(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam, position=posit, image=imgg, Detail=detai, facebook=face,
                                     linkedin=linkedi, instagram=insta, twitter=twitt)
            return redirect('admin_home4')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_STORE.objects.filter(id=1)
            bans.update(Discription=posit)
            return redirect('admin_home4')
    test = TESTIMONY.objects.all()
    ban = BANNER_STORE.objects.get(id=1)
    d = {"test": test, "ban": ban}
    return render(request, 'admin_home4.html', d)


def ADMIN_CAMPS(request):
    if request.method == "POST":
        if 'cpma' in request.POST:
            c = request.POST
            cname = c['cmpp']
            dayy = c['day']
            strdte = c['strda']
            dimg = request.FILES['img']
            sdeta = c['det']
            text = c['about']
            Camps.objects.create(camp_name=cname, no_of_days=dayy, date=strdte, image=dimg, detail=sdeta, content=text)
    camp = Camps.objects.all()
    d = {"camp": camp}
    return render(request, 'admin_camps.html', d)


def ADMIN_NEWS(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        NEWSS.objects.create(Year=nyear, image=nimg)
    camp = Camps.objects.all()
    fir = NEWSS.objects.filter(Year="2018")
    sec = NEWSS.objects.filter(Year="2018")
    thi = NEWSS.objects.filter(Year="2019")
    fou = NEWSS.objects.filter(Year="2020")
    fiv = NEWSS.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv, "camp": camp}
    return render(request, 'admin_news.html', d)


def ADMIN_GALLERY(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        GALLERY.objects.create(Year=nyear, image=nimg)
    camp = Camps.objects.all()
    fir = GALLERY.objects.filter(Year="2018")
    sec = GALLERY.objects.filter(Year="2018")
    thi = GALLERY.objects.filter(Year="2019")
    fou = GALLERY.objects.filter(Year="2020")
    fiv = GALLERY.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv, "camp": camp}
    return render(request, 'admin_gallery.html', d)


def ADMIN_BLOGS(request):
    if request.method == "POST":
        bcat = request.POST['cat']
        bhead = request.POST['head']
        bimg = request.FILES['img']
        bdet = request.POST['det']
        btxt = request.POST['txt']
        btag = request.POST['tag']
        BLOGS.objects.create(category=bcat, Heading=bhead, image1=bimg, Detail=bdet, Discription=btxt, tags=btag)
    bl = BLOGS.objects.all()
    d = {"bl": bl}
    return render(request, 'admin_blogs.html', d)


def ADMIN_EVENTS(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        EVENTSS.objects.create(Year=nyear, image=nimg)
    camp = Camps.objects.all()

    fir = EVENTSS.objects.filter(Year="2018")
    sec = EVENTSS.objects.filter(Year="2018")
    thi = EVENTSS.objects.filter(Year="2019")
    fou = EVENTSS.objects.filter(Year="2020")
    fiv = EVENTSS.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv, "camp": camp}
    return render(request, 'admin_events.html', d)


#####     admin delete ####

def ADMIN_GALLERY_DELETE(request, del_id):
    GALLERY.objects.get(id=del_id).delete()
    return redirect('admin_gallery')


def ADMIN_NEWS_DELETE(request, del_id):
    NEWSS.objects.get(id=del_id).delete()
    return redirect('admin_news')


def ADMIN_EVENTS_DELETE(request, del_id):
    EVENTSS.objects.get(id=del_id).delete()
    return redirect('admin_events')


def ADMIN_BLOGS_DYNAMICC_DELETE(request, del_id):
    BLOGS.objects.get(id=del_id).delete()
    return redirect('admin_blogs')


def ADMIN_TEAM_DELETE(request, del_id):
    Team.objects.get(id=del_id).delete()
    return redirect('admin_about')


def ADMIN_TESTIMONY_DELETE(request, del_id):
    TESTIMONY.objects.get(id=del_id).delete()
    return redirect('admin_home')


def ADMIN_CAMPS_DELETE(request, del_id):
    Camps.objects.get(id=del_id).delete()
    return redirect('admin_camps')


def ADMIN_PARTICPANT_DELETE(request, del_id):
    CAMPparticipants.objects.get(id=del_id).delete()
    return redirect('admin_camps')

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

