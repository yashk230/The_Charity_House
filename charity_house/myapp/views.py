import razorpay
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import (connected_donor, connected_ngos, daily, food, money, ngo,
                     ngo_details, user_details)

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

####################################################
def registration(request):
    return render (request,'registration.html')
    
def who_are_we(request):
    return render(request,'who.html')

def what_we_do(request):
    return render(request,'what.html')

def registration_ngo(request,did):
    context={}
    context['donor']=int(did)
    if int(did)==1:
        if request.method=="POST":
            n=request.POST["email"]
            p=request.POST["pass"]
            cp=request.POST["cpass"]
            # print(p,n,cp)######Donor
            if n=="" or p=="" or cp=="":
                context["error_message"]="Fields can not be emplty please fill the fields"
                return render(request,'registration.html',context)
            elif p!=cp:
                context["error_message"]="Password and conform password sholud be same"
                return render(request,'registration.html',context)
            else:
                u=User.objects.create(username=n,email=n)
                u.set_password(p)
                u.save()
                context["Sucess"]="Regestration Successfull now you can login"
            return redirect('/login',context)
        else:
            return render(request,'registration.html',context)
    else:
        if request.method=="POST":
            n=request.POST["email"]
            p=request.POST["pass"]
            cp=request.POST["cpass"]
            # print(p,n,cp) ########## NGO
            if n=="" or p=="" or cp=="":
                context["error_message"]="Fields can not be emplty please fill the fields"
                return render(request,'registration.html',context)
            elif p!=cp:
                context["error_message"]="Password and conform password sholud be same"
                return render(request,'registration.html',context)
            else:
                # if request.user.is_authenticated:
                # ui=User.objects.filter(id=user.id)
                u=User.objects.create(username=n,email=n)
                u.set_password(p)
                u.save()
                # print(u)
                context["Sucess"]="Regestration Successfull now you can login"
                # with transaction.atomic():
                #     retrive=n
                #     source=User.objects.get(email=retrive)
                #     destination=ngo_details(email=source.email)
                #     destination.save()
                #     d=User.objects.filter(id=request.user.id)
                #     d.delete()
                return redirect('/ngo_login',context)
        else:
            return render(request,'registration.html',context)

####################################################

def fpass(request):
    context={}
    if request.method=="POST":
            n=request.POST["email"]
            p=request.POST["pass"]
            cp=request.POST["cpass"]
            # print(p,n,cp)######Donor
            if n=="" or p=="" or cp=="":
                context["error_message"]="Fields can not be emplty please fill the fields"
                return render(request,'registration.html',context)
            elif p!=cp:
                context["error_message"]="Password and conform password sholud be same"
                return render(request,'registration.html',context)
            else:
                for u in User.objects.filter(email=n):
                    # u=User.objects.filter(email=n)
                    u.set_password(p)
                    u.save()
                context["Sucess"]="Password Updated Successfull now you can login"
            return redirect('/login',context)
    return render(request,'fpass.html')



#####################################################
def ulogin(request):
    context={}
    if request.method=="POST":
        
        n=request.POST["email"]
        p=request.POST["pass"]
        if n=="" or p=="":
            context["error_message"]="Fields can not be emplty please fill the fields"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=n,password=p)
            if u is not None:
                login(request,u)
                if request.user.is_authenticated:
                    u=User.objects.filter(id=request.user.id)
                    if user_details.objects.filter(email=request.user.email).exists():
                        return redirect('/dashboard_user')
                    else:
                        destination=user_details.objects.create(email=n,d_id=u[0])
                        destination.save()
                        return redirect('/dashboard_user')
                return redirect('/dashboard_user')
            else:
                context['error']='Username and password not matched'
                return render(request,'login.html',context)
            return redirect('/dashboard')
    return render(request,'login.html')

def ulogout(request):
    logout(request)
    return redirect('/index')
######################################################

def index(request):
    # print(request.user.is_authenticated)
    return render(request,'index.html')
#######################################################
def ngos_connected(request):    ###to display the conneted ngos
    context={}
    
    if connected_ngos.objects.filter(c_id=request.user.id):
        context['connect']=connected_ngos.objects.filter(c_id=request.user.id)
    else:
        context['no']="Sorry You are not connected to any NGO"
    # for obj in connected_ngos.objects.all():
    #     a=obj.c_id.id = request.user.id
    #     print("yash",a)
    
    return render(request,'ngos_connected.html',context)

def new_ngo(request):
    context={}
    obj=ngo_details.objects.all()
    for n in ngo_details.objects.all():
        if connected_ngos.objects.filter(n_id=n.id):
            context['a']="CONNECTED"
    context['ngo']=obj
    return render(request,'new_ngo.html',context)

#########################################################
def ngo_detail(request,nid):
    context={}
    detail=ngo_details.objects.filter(id=int(nid))
    
    # list1=ngo_details.objects.all()
    # list2=connected_ngos.objects.all()
    # list_name=[]
    # name_list=[]
    # for x in list1:
    #     list_name.append(x.email)
    # for y in list2:
    #     name_list.append(y.email)
    # if any(item in list_name for item in name_list):
    #     context['error']="Ngo Already added"
    #     return render(request,'ngo_details.html',context)
    # else:
    #     for ngo in ngo_details.objects.filter(id=int(nid)):
    #         connected_ngos.objects.create(name=ngo.name,email=ngo.email,address=ngo.address,category=ngo.category,works=ngo.works,awards=ngo.awards,pimage=ngo.pimage)
    # return render(request,'ngo_details.html',context)
    context['ngo']=detail
    return render(request,'ngo_details.html',context)
##############################################

def ngo_connect(request,nid): ##when user clicks on the connect to ngo button
    context={}
    if request.user.is_authenticated:
        u=User.objects.filter(id=request.user.id)
        print("yash",u)
        # n=ngo_details.objects.filter()
        # for ngo in ngo_details.objects.filter(id=int(nid)):
        n=ngo_details.objects.filter(id=int(nid)).first()
        # q=connected_ngos.objects.filter(n_id =n)[:1]
        if connected_ngos.objects.filter(n_id = n, c_id=request.user.id):#q.exists():
            context['msg']='Ngo already exists'
        else:
            context['msg']='Ngo Added Successfully'
            connected_ngos.objects.create(c_id=u[0],n_id=n)
        
        # for use in user_details.objects.filter(d_id=request.user.id):
        if connected_donor.objects.filter(ngo_id=n,d_id=request.user.id):#.exists():
            context['msg']='Ngo already exists'
        else:
            context['msg']='Ngo Added Successfully'
            connected_donor.objects.create(d_id=u[0],ngo_id=n)
        return render(request,'ngo_details.html',context)

##################################################
def dashboard_user(request):
    context={}
    if request.user.is_authenticated:
        a=connected_donor.objects.filter(d_id=request.user.id).count()
        context['a']=a
        
        a=food.objects.filter(userid=request.user.id).count()
        b=daily.objects.filter(userid=request.user.id).count()
        context['count']=a+b
    return render(request,'dashboard_user.html',context)


def user_profile(request):
    if request.user.is_authenticated:
        context = {}
        # user = User.objects.filter(id = request.user.id)
        # context['data'] = user
        obj=user_details.objects.filter(d_id=request.user.id)
        context['donor']=obj
        if request.method == "POST":
            n= request.POST.get('name')
            e= request.POST.get('email')
            p= request.POST.get('phone')
            a= request.POST.get('address')
            # user_details.objects.update(name=n,email=e,phone=p,address=a)
            obj.update(name=n,email=e,phone=p,address=a)
            context['msg']="Data Updated sussfully "
    return render(request,'user_profile.html',context)

def update_pass(request):
    context={}
    if request.method=="POST":
        p=request.POST.get('cpass')
        np=request.POST.get('npass')
        for u in User.objects.filter(password=p):
            u.set_password(np)
    return render(request,'user_profile.html',context)
    

###############################################################

def make_donations(request):
    context={}
    context['ngo']=connected_ngos.objects.filter(c_id=request.user.id)
    return render(request,'make_donations.html',context)

def donate(request,nid):
    context={}
    context['nid']=nid
    return render(request,'donate.html',context)

############### To make donation             ###################
# def money_donate(request,nid):
#     # print("money",nid)
#     context={}
#     context['id']=ngo_details.objects.filter(id=nid)
#     if request.method == 'POST':
#         amount = int(request.POST.get('amount')) * 100  # Convert to paise
#         client = razorpay.Client(auth=("rzp_test_JjQ72OskgZ3YwQ", "Wve5BMxfecpjBRVbi04U19sj"))
#         payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
#         return render(request,'money_donate.html', {'payment': payment})
#     return render(request,'money_donate.html',context)



def initiate_payment(request,nid):
    if request.method == "POST":
        amount = int(request.POST['amount']) * 100  # Convert to paise
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        
        order = money.objects.create(
            user=request.user,
            amount=amount / 100,
            razorpay_order_id=payment['id'],
            ngo_id=nid
        )
        order.save()
        
        context = {
            'order': order,
            'payment': payment,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID
            
        }
        return render(request, 'payment.html', context)
    return render(request, 'initiate_payment.html')

def verify_payment(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        
        order = money.objects.get(razorpay_order_id=razorpay_order_id)
        order.razorpay_payment_id = razorpay_payment_id
        order.razorpay_signature = razorpay_signature
        order.paid = True
        order.save()
        
        return render(request, 'initiate_payment.html')
    return redirect('initiate_payment')

##################  Daily Essentials        ####################
def daily_donate(request,nid):
    print("daily",nid)
    context={}
    for a in user_details.objects.filter(d_id=request.user.id):
        addr=a.address
    if request.user.is_authenticated:
        u=User.objects.filter(id=request.user.id)
        if request.method == "POST":
            t=request.POST.get('type')
            i=request.POST.get('items')
            print(t,i)
            daily.objects.create(type=t,items=i,Address=addr,userid=u[0],ngo_id=nid)
    return render(request,'daily_donate.html',context)

##################################################################

def food_donate(request,nid):
    print("food",nid)
    if request.method=="POST":
        i=request.POST["item"]
        p=request.POST["place"]
        t=request.POST["time"]
        s=request.POST["serving"]
        e=request.POST["expire"]
        a=request.POST["address"]
        if request.user.is_authenticated:
            u=User.objects.filter(id=request.user.id)
            food.objects.create(Item=i,Place=p,Time=t,Serving=s,Expire=e,Address=a,userid=u[0],ngo_id=nid)
    return render(request,'food_donate.html')



def donations_made(request):
    context={}
    moneye=money.objects.filter(user=request.user.id , paid=1)
    context['money']=moneye
    foode=food.objects.filter(userid=request.user.id)
    context['food']=foode
    dailyy=daily.objects.filter(userid=request.user.id)
    context['daily']=dailyy
    return render(request,'donations_made.html',context)
    
        

#############################################

############# NGO Part ######################

#############################################
def nlogin(request):
    context={}
                    ### Ngo login and if loged in 1st time save in the ngo_details db
    if request.method=="POST":
        n=request.POST["email"]
        p=request.POST["pass"]
        if n=="" or p=="":
            context["error_message"]="Fields can not be emplty please fill the fields"
            return render(request,'ngo_login.html',context)
        else:
            u=authenticate(username=n,password=p)
            if u is not None:
                login(request,u)
                if request.user.is_authenticated:
                    u=User.objects.filter(id=request.user.id)
                    if ngo.objects.filter(email=request.user.email).exists():
                        ngo.objects.filter(email=request.user.email).delete()
                        return redirect('/dashboard_ngo')
                    else:
                        destination=ngo.objects.create(email=n,n_id=u[0])
                        destination.save()
                        return redirect('/dashboard_ngo')
                return redirect('/dashboard_ngo')
            else:
                context['error']='Username and password not matched'
                return render(request,'ngo_login.html',context)
            return redirect('/dashboard')
    return render(request,'ngo_login.html')

def nlogout(request):
    logout(request)
    return redirect('/index')

#######################################################

def ngo_profile(request):
    context = {}
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    print(b)
    context['id']=b
    
    u=User.objects.filter(id=request.user.id)
    context['new']=ngo_details.objects.filter(email = request.user.email)
    objj=ngo.objects.filter(email = request.user.email)
    context['ngo']=objj
    if request.method=="POST" :
        n=request.POST["name"]
        e=request.POST["email"]
        a=request.POST["address"]
        c=request.POST["category"]
        w=request.POST["works"]
        aw=request.POST["awards"]
        i=request.FILES["image"]
        ngo_details.objects.create(name=n,email=e,address=a,category=c,works=w,awards=aw,pimage=i,u_id=u[0])
        ngo.objects.filter(email = request.user.email).delete()
    return render(request,'ngo_profile.html', context)


def dashboard_ngo(request):
    context={}
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    if a is None:
        print("is",a)
    else:
        b=a['u_id']
        context['id']=b
        
    aa=ngo.objects.filter(n_id=request.user.id).values('n_id').first()
    if aa is None:
        print("")
    else:
        bb=aa['n_id']
        context['id']=bb
    
    if request.user.is_authenticated:
        # if connected_donor.objects.filter(ngo_id=request.user.id):
        print("user",request.user.id)
        for n in ngo_details.objects.filter(u_id=request.user.id):
            print(n.u_id)
        
        
        for a in connected_donor.objects.filter(ngo_id=request.user.id):
            print(a.d_id)
            a=user_details.objects.filter(d_id=a.d_id).count()
            context['count']=a
    return render(request,'dashboard_ngo.html',context)


def donation_request(request):
    context={}
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    # print(b)
    context['id']=b
    for n in ngo_details.objects.filter(u_id=request.user.id):
        f=food.objects.filter(ngo_id=n.id,Status="UnResponded")
        context['f']=f
        ff=daily.objects.filter(ngo_id=n.id,Status="UnResponded")
        context['c']=ff
    return render(request,'donation_request.html',context)

def donation_request_update_food(request,did):   # data from the form is collected in this view
    print("yash",did)
    # if food.objects.filter(id=did):
    if request.method == "POST":
        if food.objects.filter(id=did):
            f=food.objects.filter(id=did)
            s=request.POST.get("status")
            i=request.POST.get("entry_id")
            print("ID",i)
            # print("status",s)
            if s == "Rejected":
                print("this is working")
                f.update(Status="Rejected")
            else:
                f.update(Status="Accepted")
    return redirect('/donation_request')

                
def donation_request_update_daily(request,did):   # data from the form is collected in this view
    print("yash",did)
    # if food.objects.filter(id=did):
    if request.method == "POST":
        if daily.objects.filter(id=did):
            f=daily.objects.filter(id=did)
            s=request.POST.get("status")
            i=request.POST.get("entry_id")
            print("ID",i)
            print("status",s)
            if s == "Rejected":
                print("this is working")
                f.update(Status="Rejected")
            else:
                f.update(Status="Accepted")
                
    return redirect('/donation_request')


def to_be_received(request):
    context={}
    
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    print(b)
    context['id']=b
    
    for n in ngo_details.objects.filter(u_id=request.user.id):
        f=food.objects.filter(ngo_id=n.id,Status="Accepted")
        context['f']=f
        ff=daily.objects.filter(ngo_id=n.id,Status="Accepted")
        context['c']=ff
        
    return render(request,'to_be_received.html',context)

def to_be_received_food(request,did):   # data from the form is collected in this view
    print("yash",did)
    # if food.objects.filter(id=did):
    if request.method == "POST":
        if food.objects.filter(id=did):
            f=food.objects.filter(id=did)
            s=request.POST.get("status")
            i=request.POST.get("entry_id")
            print("ID",i)
            print("status",s)
            if s == "Received":
                print("this is working")
                f.update(Status="Received")
    return redirect('/to_be_received')

                
def to_be_received_daily(request,did):   # data from the form is collected in this view
    print("yash",did)
    # if food.objects.filter(id=did):
    if request.method == "POST":
        if daily.objects.filter(id=did):
            f=daily.objects.filter(id=did)
            s=request.POST.get("status")
            i=request.POST.get("entry_id")
            print("ID",i)
            print("status",s)
            if s == "Received":
                print("this is working")
                f.update(Status="Received")
                
    return redirect('/to_be_received')

def donations_received(request):
    context={}
    
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    print(b)
    context['id']=b
    
    for n in ngo_details.objects.filter(u_id=request.user.id):
        context['f']=food.objects.filter(ngo_id=n.id,Status="Received")
        context['c']=daily.objects.filter(ngo_id=n.id,Status="Received")
    return render(request,'donations_received.html',context)

def donations_rejected(request):
    context={}
    
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    print(b)
    context['id']=b
    
    for n in ngo_details.objects.filter(u_id=request.user.id):
        context['f']=food.objects.filter(ngo_id=n.id,Status="Rejected")
        context['c']=daily.objects.filter(ngo_id=n.id,Status="Rejected")
    return render(request,'rejected.html',context)

########################################################3

def ngo_login(request):
    return render(request,'ngo_login.html')

def work_done(request):
    context={}
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    print(b)
    context['id']=b
    
    return render(request,'work_done.html',context)

def ngo_details_work(request,wid):
    context={}
    context['work']=int(wid)
    return render(request,'ngo_details.html',context)

def donor_connected(request):
    context={}
    
    a=ngo_details.objects.filter(u_id=request.user.id).values('u_id').first()
    b=a['u_id']
    # print(a,'one',b)
    context['id']=b
    
    if request.user.is_authenticated:
        if ngo_details.objects.filter(u_id=request.user.id):
            a=ngo_details.objects.filter(u_id=request.user.id).values('id')
            b=a[0]['id']
            for c in connected_donor.objects.filter(ngo_id=b):
                print("user",c.d_id)
                context['donor']=user_details.objects.filter(d_id=c.d_id)
                print(context)
                # print(context)
    return render(request,'donor_connected.html',context)
###############################################

def contact(request):
    return render(request,'contact.html')

def admin_pannel(request):
    return render(request,'admin_pannel.html')
