from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from random import randrange
from todo_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import TaskModel
from .forms import TaskForm
#from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        em = request.POST.get('em')
        try:
            usr = User.objects.get(username = un)
            return render(request, 'signup.html',{'msg': 'Username Already Exists'})
        except User.DoesNotExist:
            try:
                usr = User.objects.get(email=em)
                return render(request, 'signup.html',
                              {'msg': 'Email Already Exists'})
            except User.DoesNotExist:
                text = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
                pw = ''
                for i in range(4):
                    pw = pw + text[randrange(len(text))]
                print(pw)
                send_mail('Welcome to To-Do List', 'Your password is : '+ pw, EMAIL_HOST_USER, [em])
                usr = User.objects.create_user(username = un, password = pw, email = em)
                usr.save()
                return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        usr = authenticate(username=un, password=pw)
        if usr is None:
            return render(request, 'signup.html',{'msg': 'Invalid Credentials'})
        else:
            auth_login(request, usr)
            return redirect('viewtask')
    else:
        return render(request, 'login.html')


def resetpassword(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        em = request.POST.get('em')
        try:
            usr = User.objects.get(username=un) and User.objects.get(email = em)
            text = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
            pw = ''
            for i in range(4):
                pw = pw + text[randrange(len(text))]
            print(pw)
            send_mail('Welcome to To-Do List', 'Your password is : '+ pw, EMAIL_HOST_USER, [em])
            usr.set_password(pw)
            usr.save()
            return redirect('login')
        except User.DoesNotExist:
            return render(request, 'resetpassword.html',
                          {'msg': 'Invalid Credentials'})
    else:
        return render(request, 'resetpassword.html')


def changepassword(request):
    if request.method == 'POST':
        u1 = request.user.username
        print(u1)
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if pw1 == pw2:
            usr = User.objects.get(username=u1)
            usr.set_password(pw1)
            usr.save()
            return redirect('login')
    else:
        return render(request, 'changepassword.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

def viewtask(request):
    user = request.user
    print(user)
    data = TaskModel.objects.filter(user=request.user)
	#task = TaskModel.objects.filter(owner=request.user)
    #data = TaskModel.objects.all()
    return render(request,'viewtask.html',{'data' : data})

#@login_required(login_url='login/')
def createtask(request):
    if request.method == 'POST':
        user = request.user
        f = TaskForm(request.POST)
        if f.is_valid():
            em = request.user.email
            print (em)

            todo = f.save(commit=False)
            todo.user = user
            todo.save()
            fm = TaskForm()
            return render(request, 'createtask.html', {'fm': fm,
                          'msg': 'Task Added'})
        else:
            return render(request, 'createtask.html', {'fm': f,
                          'msg': 'Check Errors'})
    else:
        fm = TaskForm()
        return render(request, 'createtask.html', {'fm': fm})

def delete(request,id):
	#ds = TaskModel.objects.get(tid = id)
	#em = request.user.email
	
	#send_mail('Welcome to To-Do List', 'Congratulation for completing your task', EMAIL_HOST_USER, ['em'])
	# ds.delete()
	# return redirect('viewtask')
    print(id)
    ds = TaskModel.objects.get(pk = id)
    ds.delete()
    return redirect('viewtask')
	
