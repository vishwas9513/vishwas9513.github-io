from django.shortcuts import render
from .models import job
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import profile
# Create your views here.
def list_job(request):
    object_list=job.objects.all()
    return render(request,'jobapp/list.html',{'object_list':object_list})
def jobdetail(request,id):
    idd=job.objects.get(id=id)
    return render(request,'jobapp/jobdetail.html',{'data':idd})

def register(request):
    if request.method=='POST':
        fn=UserCreationForm(request.POST)
        print(fn)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password1']
            u1=User.objects.create(username=uname,password=upass)
            u1.save()
            return redirect("/login") 
            
    else:
        fn=UserCreationForm()
    return render(request,"jobapp/signup.html",{'form':fn})  

def user_login(request):
    if request.method=='POST':
        fn=AuthenticationForm(request=request,data=request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            print(u)
            if u is not None:
                login(request,u)
                return render(request,'jobapp/list.html')
    else:
        fn=AuthenticationForm()
    return render(request,'jobapp/login.html',{'form':fn})

def user_profile(request):
    return render(request,'jobapp/profile.html')
def user_form(request):    
        # jb=AuthenticationForm(request=request,data=request.POST)
        if request.method=='POST':
            jb=profile(request,'POST')
           
            if jb.is_valid():
             jb.save()
            jb=profile()

            
            # jname=request.POST['Name']
            # jsurname=request.POST['Surname']
            # jheadline=request.POST['Headline']
            # jcurrent_position=request.POST['Current Position']
            # jeducation=request.POST['Education']
            # jcountry=request.POST['Country']
            # jstate=request.POST['State/Region']
            # jb=authenticate[name=jname,surname=jsurname,headline=jheadline,current_postion=jcurrent_position,education=jeducation,country=jcountry,state=jstate]
            # jb=profile.objects.create(name=jname,surname=jsurname,headline=jheadline,current_postion=jcurrent_position,education=jeducation,country=jcountry,state=jstate)
            # jb.save()
        # return HttpResponse('profile_saved successfully')
    # else:
    #     jb=user_profile
    # return render(request,'jobapp/login.html')       
    # return redirect('jobapp/profile.html')
    # return render(request,'petsapp/profile.html')
def user_logout(request):
    logout(request)
    return redirect('/login')
# def register(request):
#     if request.method == 'POST':
#         fn = signupform(request.POST)
#         if fn.is_valid():
#             fn.save()
#             return redirect("/login")  # Redirect to the login page after successful signup
#     else:
#         fn = signupform()
#     return render(request, 'petsapp/signup.html', {'form': fn})

# def user_login(request):
#     if request.method=='POST':
#         fn=AuthenticationForm(request=request,data=request.POST)
#         if fn.is_valid():
#             uname=fn.cleaned_data['username']
#             upass=fn.cleaned_data['password']
#             u=authenticate(username=uname,password=upass)
#             print(u)
#             if u is not None:
#                 login(request,u)
#                 return render(request,'petsapp/list.html')
#     else:
#         fn=AuthenticationForm()
        
#     return render(request,'petsapp/login.html',{'form':fn})
      


