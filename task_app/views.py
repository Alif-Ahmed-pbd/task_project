from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import*
from .forms import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = Custom_user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = Custom_user_form()
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form=SigninForm()
    return render(request, 'signin.html',{'form':form})

@login_required
def home(request):
    
    return render (request, 'home.html')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required

def update_profile(request):
    if request.method=='POST':
        form =User_Profile_from(request.POST)
        if form.is_valid():
            co=form.save(commit=False)
            co.user=request.user
            co.save()
            return redirect('profile')
    else:
        form=User_Profile_from()
    return render(request, 'up_profile.html', {'form':form})

@login_required

def profile(request):
    prof=User_Profile.objects.all()
    context={
        'user':prof
    }
    return render(request, 'profile.html', context)

@login_required

def edit_profile(request):
    user_profile=0
    try:
        user_profile=User_Profile.objects.get(user=request.user)
    except:
        pass
    if request.method=='POST':
        form = User_Profile_from(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=User_Profile_from(instance=user_profile)
    return render(request, 'up_profile.html', {'form':form})

@login_required
def user_delete(request, id):
    prof=User_Profile.objects.filter(id=id)
    prof.delete()
    return redirect('profile')

@login_required
def addtask(request):
 
    if request.method=='POST':
        form = Add_task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = Add_task_form()
    return render(request, 'addtask.html', {'form':form})

@login_required
def tasklist(request):
    all_task = Add_task.objects.filter()
    return render(request, 'tasklist.html', {'all_task':all_task})

@login_required
def edittask(request, id):
    task=Add_task.objects.get(id=id)
    if request.method=='POST':
        form=Add_task_form(request.POST,instance=task)
        if form.is_valid():
            co=form.save(commit=False)
            co.user=request.user
            co.save()
            return redirect('tasklist')
    else:
        form=Add_task_form(instance=task)
    return render(request, 'addtask.html', {'form':form})


@login_required
def deletetask(request, id):
    task=Add_task.objects.get(id=id)
    task.delete()
    return redirect('tasklist')

@login_required
def task_completed(request, id):
    task = get_object_or_404(Add_task, pk=id)
    
    task.completion_status = True
    
    task.save()
    
    return redirect('tasklist')


@login_required
def proggraming(request):
    tasks = Add_task.objects.filter(task_categorie='proggraming').order_by('user')
    context = {
        'tasks': tasks
    }
    return render(request, 'proggraming.html', context)

@login_required
def practice(request):
    tasks = Add_task.objects.filter(task_categorie='practice').order_by('user')
    context = {
        'tasks': tasks
    }
    return render(request, 'practice.html', context)

@login_required
def contest(request):
    tasks = Add_task.objects.filter(task_categorie='contest').order_by('user')
    context = {
        'tasks': tasks
    }
    return render(request, 'contest.html', context)



from django.db.models import Q
@login_required
def search_query(request):
    search_post = Add_task.objects.none()  
    if request.method == 'POST':
        query = request.POST.get('search')
        search_post = Add_task.objects.filter(
            Q(task_title__icontains=query) | Q(task_description__icontains=query)
        )
    return render(request, 'search.html', {'sq': search_post})

