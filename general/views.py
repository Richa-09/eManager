from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, board, checklist, card
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'general/home.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.info(request,"Username/Password invalid")
            return render(request,'general/login.html')
    return render(request,'general/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        bio = request.POST['bio']
        try:
            user=User.objects.get(username=name)
        except:
            if pwd1 != pwd2:
              messages.info(request,"Password don't match")
              return render(request,'general/signup.html')
            if len(pwd1)<8:
                messages.info(request,"Password is too short")
                return render(request,'general/signup.html')
            us = User()
            us.username = name
            us.email = email
            us.set_password(pwd1)
            us.save()

            p=UserProfile()
            user = User.objects.get(username=name)
            p.user = user
            p.bio = request.POST['bio'] 
            p.save()

            messages.success(request,"Signed up successfully")
            return redirect('login_page')
        else :
            messages.info(request,"Username already exists")
            return render(request,'general/signup.html')
    return render(request,'general/signup.html')

@login_required(login_url='login_page')
def logoutUser(request):
    logout(request)
    return render(request,'general/home.html')

@login_required(login_url='login_page')
def newboard(request):
    return render(request,'general/newboard.html')

@login_required(login_url='login_page')
def dashboard(request):
    boardss = board.objects.all().filter(user=request.user)
    return render(request,'general/boards.html',{'boardss':boardss})

@login_required(login_url='login_page')
def create_board(request):
    if request.method == 'POST':
        b=board()
        b.title = request.POST['title']
        b.detail = request.POST['description']
        b.user = request.user
        b.save()
        return redirect('dashboard')
    else:
        return redirect('home_page')

@login_required(login_url='login_page')
def listpage(request,k):
    lists = checklist.objects.all().filter(board=k)
    cards = card.objects.all()
    return render(request,'general/listpage.html',{'lists':lists,'cards':cards,'k':k})

@login_required(login_url='login_page')
def create_list(request,k):
    if request.method == 'POST':
        c = checklist()
        c.name = request.POST['title']
        c.board = board.objects.all().filter(id=k)[0]
        c.save()
        return redirect('listpage', k=k)
    else:
        return redirect('home_page')

@login_required(login_url='login_page')
def create_card(request,k,p):
    if request.method == 'POST':
        d = card()
        d.name = request.POST['name']
        d.checklist = checklist.objects.all().filter(id=p)[0]
        d.save()
        return redirect('listpage', k=k)
    else:
        return redirect('home_page')

@login_required(login_url='login_page')
def del_board(request,z):
    ll = board.objects.all().filter(pk=z)
    ll.delete()

    return redirect('dashboard')

@login_required(login_url='login_page')
def del_list(request,k,p):
    ll = checklist.objects.all().filter(pk=p)
    ll.delete()

    return redirect('listpage',k=k)

@login_required(login_url='login_page')
def del_card(request,k,p,z):
    ll = card.objects.all().filter(pk=z)
    ll.delete()

    return redirect('listpage',k=k)