from django.shortcuts import render,redirect
import re
from app1.models import detail
# Create your views here.
def user_account(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        u_msg=p_msg=m_msg=e_msg=""

        if not username:
            u_msg="Username is required."
        elif not re.match(r'[A-Za-z ]',username):
            u_msg="Only alphabets and spaces are allowed."
        elif len(username)<3:
            u_msg="Name is too short (min 3 chars)."
        if not password:
            p_msg="Password cannot be empty."
        elif len(password)<6:
            p_msg="Security alert: Password must be at least 6 characters long."
        if not email:
            e_msg="Email address is required."
        elif not email.endswith('@gmail.com') or len(email) < 11:
            e_msg="Please enter a valid @gmail.com address."
        if not mobile:
            m_msg="Mobile number is required."
        elif not re.fullmatch(r'[6-9][0-9]{9}',mobile):
            m_msg= "Enter a valid 10-digit Indian mobile number (starting with 6-9)."
        
        if u_msg or p_msg or e_msg or m_msg:
            return render(request,'signup.html',{'msg_username':u_msg,
                                                 'msg_pwd':p_msg,
                                                 'msg_m':m_msg,
                                                 'msg_email':e_msg ,
                                                 'u':username,
                                                 'm':mobile,
                                                 'e':email})
        query=detail.objects.create(username=username,password=password,email=email,mobile=mobile)
        return redirect('login')
    return render(request,'signup.html')


def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        query1=detail.objects.filter(username=username ,password=password).first()
        if query1:
            return redirect('dashboard',id=query1.id)
        else:
            return render(request,'login.html',{'msg':'Invalid Username and Password','u':username})
    return render(request,'login.html')

def dashboard(request,id):
    query=detail.objects.get(id=id)
    response=render(request,'dashboard.html',{'user_id':query})
    return response