from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login
from .models import .

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method=="POST":
        pass

    return render(request, 'login.html')

def register(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            name = userObj['name']
            email =  userObj['email']
            username = email
            password =userObj['password']
            confirm = userObj['confirmpass']
            print("Username and password and confirmpassword is as follows:- ", username,password,confirm)
            if(password==confirm):
                subject = "Registration for Breeze 18 successful."
                message = "Welcome to Breeze 18 by SNU. "
                from_email = settings.EMAIL_HOST_USER
                to_list = [email, settings.EMAIL_HOST_USER]
                print(os.getcwd())
                html_message = loader.render_to_string(
                    os.getcwd()+'/Breeze/templates/SigningupMail.html',
                    {
                        # 'user_name': username,
                        # 'subject': 'Thank you for registering with us '+username+' \n You will now be recieving Notifications for howabouts at SNU in an all new Way. Goodbye to the spam mails. \n Thanks for registering. Have a nice day!!',
                        # 'linkTosite': 'www.google.com',
                    }
                )
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    Profile = Profile.objects.create(id=x.id + 1, Name=name, Username=username,
                                                                Email=email, Password=password, interests="")
                    print("User created Successfully")

                    print("falana dhamaka")
                try:

                    send_mail(subject, message, from_email, to_list, fail_silently=False, html_message=html_message)
                except:
                    print("Mail not sent")
        return HttpResponseRedirect(redirect_to)




def login_view(request):
   redirect_to = request.REQUEST.get('next', '')
   if request.method=='POST':
      #create login form...
      if valid login credentials have been entered:
         return HttpResponseRedirect(redirect_to)
   #...
   return render_to_response('login.html', locals())
