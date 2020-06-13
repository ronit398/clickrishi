from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def Signup(request):

    if request.method == 'POST':        
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        username = request.POST['username']
        
        msgToSend = "Welcome" + " " +firstName+ "," + "\n\n" + "Thanks For joining us. We are so happy you are here, We Founded ClickRishi because we wanted to create a better oppurtunity for you and for your Crops\n\n\nTeam ClickRishi."
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Taken')
            return redirect(Signup)
        
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken')
            return redirect(Signup)
        
        else:
            x = User.objects.create_user(first_name = firstName,last_name = lastName,email = email,password=password,username=username)
            x.save()
            send_mail(
                'Hurray! Welcome to ClickRishi, You Joined your team and ours',
                msgToSend,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            
            return redirect('/')
            
    else:
        return render(request,'SignUp.html')

