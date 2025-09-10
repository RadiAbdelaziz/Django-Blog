from django.shortcuts import render , redirect
from accounts.forms import RegisterForm , UpdatedForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login , logout
# Create your views here.


def register_view(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_post')
    else:   
        form = RegisterForm()    

    return render(req , "accounts/register.html" , {"form" : form})


def login_view(req):

    if req.method == "POST":
        form = AuthenticationForm(req , data = req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req , user)
            return redirect("show_post")
    else :
        form = AuthenticationForm()        
    return render(req , "accounts/login.html" , {"form" : form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def logout_view(req):
    logout(req)
    return render (req , "accounts/logout.html")



def updated_view(req):
    if req.method == "POST":
        form = UpdatedForm(req.POST , instance = req.user) 
        if form.is_valid():
            form.save()
            return redirect("show_post")
    else :
        form = UpdatedForm()

    return render(req, "accounts/update_user.html" , {"form" : form})    

def about_view(req):
    return render (req , "blog/about.html")