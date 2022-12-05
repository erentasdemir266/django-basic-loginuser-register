from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sitem.models import Post

# Create your views here.

def home(request):
    return render(request,"blog/home.html",)


def base(request):
    return render(request,"base.html")


def loginpage(request):
    if request.method == "POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request,"blog/login.html", {
                "error":"Username veya Parola yanlış!"
            })

    return render(request,"blog/login.html") 


def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "blog/register.html",{"error":"username kullanılıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "blog/register.html",{"error":"email kullanılıyor"})
                else:
                    user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("loginpage")
        else:
            return render(request,"blog/register.html",{"error":"parola eşleşmiyor"})    




    return render(request,"blog/register.html")

def logoutpage(request):
    logout(request)
    return redirect("loginpage")
