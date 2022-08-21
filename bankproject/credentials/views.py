from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        birth = request.POST['DOB']
        age = request.POST['AGE']
        gender = request.POST['gender']
        number = request.POST['Number']
        email = request.POST['Email']
        address = request.POST['Address']
        districts = request.POST['Select Districts']
        acc = request.POST['Account Type']
        mateerials = request.POST['Materials Required']
        if email == email:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Taken")

            user = User.objects.create_user(username=username,DOB=birth,AGE=age,gender=gender,Number=number,Email=email,Address=address,Select_Districts=districts,Account_Type=acc,Materials_Required=mateerials,email=email)
            user.save
            return redirect('/')
    return render(request,"form.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return render("register")

            user=User.objects.create_user(username=username,password=password)

            user.save();
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect ('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')