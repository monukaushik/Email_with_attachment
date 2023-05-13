from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
from django.http import HttpResponse
import openai
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(request,username=username,password=password)
      if user is not None:
         auth.login(request,user)
         if user.is_superuser:
            return redirect('/admin_panel/')
            messages.success(request,'Login Successfully !!!')
         else:
            return redirect ('/emailsend/')
      else:
            messages.error(request,'user is none')
    return render(request,'index.html')

@login_required
def generate_text(request):
    if request.method =='POST':
        input_text = request.POST.get('searchtext')
        openai.api_key = settings.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=2000,
            temperature=1,
            stop=None,
)
    generated_text = response.choices[0].text

    # return JsonResponse({'generated_text': generated_text})
    return render(request,"emailsend.html",{'data':generated_text})

@login_required
def emailsend(request):
     if request.method=='POST':
        emailto=request.POST.get('emailto')
        emailsubject=request.POST.get('emailsubject')
        emailattachment=request.FILES.get('emailattachment')
        emailbody=request.POST.get('emailbody')
     
        subject = (emailsubject[0: ])
        message = (emailbody[0: ])
        attach = (emailattachment) 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emailto]
        mail=EmailMessage( subject, message, email_from, recipient_list)
        mail.attach(attach.name,attach.read(),attach.content_type)
        mail.send()

        return redirect('/emailsend/')  
     return render(request,'emailsend.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        useremail=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password == cpassword:
            user=User.objects.create_user(username=username,email=useremail,password=password)
            user.save()
            return redirect('/')  
        else:
            messages.error(request,'password not match!!')
    return render(request,'signup.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def forgot_username(request):
    if request.method=='POST':
        username=request.POST.get('username')
        username1=User.objects.get(username=username)
        if username1 is not None:
            otp=random.randint(1000,9999)
            request.session['otp']= otp
            request.session['username']= username

            subject = 'OTP for reset password'
            message = 'This otp use for forgot password %d' % otp
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [username1.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('/forgot_otp/')
        else:
            messages.error(request,'username is none')
    return render(request,'forgot_username.html')

def forgot_otp(request):
    if request.method=='POST':
        otp= int(request.POST.get('otp'))
        session_otp=request.session.get('otp',None)
        if otp==session_otp:
            return redirect('/forgot_password/')
        else:
            return redirect('/forgot_otp/')
    return render(request,'forgot_otp.html')

def forgot_password(request):
    if request.method=='POST':
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            username=User.objects.get(username=request.session.get('username'))
            if username is not None:
                username.set_password(password)
                username.save()
                return redirect('/')
            else:
                messages.error(request,'username is none')
                return redirect('forgot_password')
        else:
            messages.error(request,'password does not match !!')       
    return render(request,'forgot_password.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')