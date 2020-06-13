__author__ = "Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"
__credits__ = ["Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"]
__version__ = "1.0.1"
__maintainer__ = "Ronit Shrivastava"
__email__ = "clickrishiteam@gmail.com"
__status__ = "Production"


from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required


#Method to load standalone page
def standalone(request):
    if request.user.is_authenticated:
        return render(request,'standalone.html')
    else:
        messages.error(request,'Login first')
        return render(request,'loginnew.html')


#Method to load test_homepage from standalone page
def standtohome(request):
    return render(request,'test_homepage.html')


#Method to load test_homepage page
def home(request):
    return render(request,'test_homepage.html')
  
  
#Method to load instructions page  
def instructions(request):
    return render(request,'instructions.html')  


#Method to register a new user in the app
def Register(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        username = request.POST['email']
        #username = request.POST['phone']
        
        #Welcome message to send to user when they signup
        msgToSend = "Welcome" + " " +firstName+ "," + "\n\n" + "Thanks For joining us. We are so happy you are here, We Founded ClickRishi because we wanted to create a better oppurtunity for you and for your Crops.\n\n\nTeam ClickRishi."
                
        
        #Cases to check if email exists in the database
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Taken')
            return redirect(Register)
        
        
        #Cases to check if username exists in the database
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Taken')
            return redirect(Register)
        
        
        #Creating user and sending Welcome Email to user's email address
        else:
            x = User.objects.create_user(first_name = firstName,last_name = lastName,email = email,password=password,username=username)
            x.save()
            send_mail(
                'Hurray! Welcome to ClickRishi, You Joined your team and ours.',
                msgToSend, 
                
                settings.EMAIL_HOST_USER,
                [username],
                fail_silently= False,
            )
            
            return redirect('/')   
    else:
        return render(request,'registration.html')
    
    
#Method to load FAQs page
def FAQs(request):
    return render(request,'faqs.html')
    
    
#Method to load Feedback page    
def Feedback(request):
    return render(request,'contactus.html')
    
    
#Method to load Aboutus page
def Aboutus(request):
    return render(request,'aboutus.html')
    
    
    
#Method for user login to the app    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
       
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            
            messages.error(request,'Username or Password Invalid')
            return redirect("Login")    
            
        
    else:
        return render(request,'loginnew.html')
        


#Method to logout user
def logout(request):
    auth.logout(request)
    return render(request,'test_homepage.html')


#Method to send feedback to Developers        
def sendFeedback(request):

    toSend = "Hello Team,\n\nWe have a Feedback from our user.\n\nUsername: "+request.POST['name']+"\n"+"Email: "+request.POST['email']+"\n\nFeedback :\n"+request.POST['msg']
    send_mail(
                'Feedback from user',
                toSend,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
    messages.success(request,'Thanks for reaching us, Your Valuable feedback is submitted.')
    return redirect(Feedback)
    
    
    
#Method to load profile page and loading the form to acccept the pic from user machines.
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if p_form.is_valid():
            p_form.save()        
            return render(request,'profile.html')
    else:
        
        p_form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'p_form': p_form        
        }
    
    return render(request,'profile.html',context)