from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')    


    else: 
        return render(request, 'login.html')   



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:  # Checking if the password is matching to entered password
            if User.objects.filter(username=username).exists(): # Checking if the username is already taken or not
                messages.info(request,'Username Taken')
                return redirect('register')  # it is inbuilt feature of django print the messages
            elif User.objects.filter(email=email).exists():  # Checking if the email exist or not 
                messages.info(request,'Email Taken')
                return redirect('register')
            else:            
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')   # User created in the database
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching') 
            return redirect('register')   # if password does not match then redirect to register page again
        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')        
