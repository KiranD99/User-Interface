from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *

def Home(request):
  form = House_Form()
  ind = request.GET.get('index',0)
  data = Houses.objects.all()
  if ind*10 > len(data):
    ind = 0
  data = data[ind*10:min((ind*10)+10,len(data))]
  if request.method == 'POST':
    a = {'name':request.POST['name'],'price':request.POST['price'],'user_id':User.objects.get(username=request.session.get('user',0))}
    form = Main_Form(a, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('Home')
  return render(request,'home.html',{'form':form,'data':data})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        response = CreateUserForm(request.POST)
        if response.is_valid():
            x = response.save()
            messages.success(request, "registration successful")
            redirect('logins')
        else:
            messages.error(request, "password must contain 8 charecters and a special character")
    context = {'form':form}
    return render(request,'register.html',context)
def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['user'] = user.get_username()
            request.session['id'] = user.id
            username = user.get_username()
            return redirect('Home')
        else:
            messages.error(request,'password or username is incorrect')
            print('oopss')
            return redirect('logins')
    return render(request,'login.html',{'register':'register'})