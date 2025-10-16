from django.shortcuts import render , redirect
from .models import Task
from collections import defaultdict
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password != password2:
            messages.error(request,'Passwprd do not matches')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
        else:
            user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('login')
    return render(request,'task/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else :
            messages.error(request,'NO found')
    return render(request,'task/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logout Succefully')
    return redirect('login')

@login_required(login_url='login')
@ensure_csrf_cookie
def index(request):
    tasks = Task.objects.filter(user = request.user).order_by('-id')
    group_task = defaultdict(list)
    for task in tasks:
        date = task.created.date()
        group_task[date].append(task)
    return render(request,'task/index.html',{'group_task':dict(group_task),'full_name':request.user.get_full_name()})

@login_required(login_url='login')
@ensure_csrf_cookie
def add_tasks(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title,user=request.user)
    return redirect('index')

@login_required
@ensure_csrf_cookie
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        is_checked = request.POST.get("complete") == "on"
        task.complete = is_checked
        task.save()
    return redirect('index')

@login_required
@ensure_csrf_cookie
def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('index')
