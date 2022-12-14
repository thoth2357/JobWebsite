from pickle import FALSE
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import * # * means all forms will get imported same for models below
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime
from django.contrib import auth


# Create your views here.

def logout(request):
    auth.logout(request)
    return render(request, 'auth/sign_out.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'auth/sign_in.html', {})

def register(request):
    if request.method == 'GET': #when you request a form it is in a get request 
        form = RegisterForm()
        context = {'form' : form} #this creates a object which you want to send to the front end
        return render(request, 'auth/sign_up.html', context) # here we pushing that form to the html page 
    
    if request.method == 'POST': #when you submit a form it is POST request
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                User.objects.create_user(
                    username = user, 
                    password = form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name']
                )
                messages.success(request, 'Account created for ' + user)
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('signup')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form' : form}
            return render(request, 'auth/sign_up.html', context)

    return render(request, 'auth/sign_up.html', {})


@login_required #This makes sure that only people who have logged in can access the profile page
def profile(request):
    user = User.objects.get(username = request.user.username)
    return render(request, 'user/profile.html' , {"user":user})

#@login_required 
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.Files) #so you will say that its the resume form but it has request.POST or request.Files, different than registerform because resume form has some file data
        if form.is_valid(): # important to this so that all form validations happen
            obj = forms.save(commit = FALSE)
            
            obj.user = request.user #this wont be null as we getting user when we logged in
            
            obj.save()
            
            messages.success(request, 'Resume Created Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error Processing your Request')
            context = {'form' : form }
            return render(request, 'create-resume.html', context)
    if request.method == 'GET':
        form = ResumeForm()
        context = {'form': form}
        return render(request, 'create-resume.html', context) # passing in context means you are passing  context = {'form': form}


class ResumeDetailView(DetailView): #class based view require must less coding compared to function based view
    model = Resume
    template_name = 'resume-detail.html'

def resume_detail(request, slug):
    obj = Resume.objects.get(slug = slug)
    
    educations =  Education.objects.filter(resume=obj) 
    context = {}  
    context['object'] = obj #we can use object... in our HTML file now with this
    context['educations'] = educations
    
    if request.method == 'POST':
        edu_form = EducationForm(request.POST)
        if edu_form.is_valid():
            o = edu_form.save(commit=False)
            
            o.resume = obj
            o.save()
            
            messages.success(request, 'Resume updated Succesfully')
            return redirect('profile')  #('resume-detail', slug = slug)
        else:
            messages.error(request, 'Error Processing your Request')
            context['edu_form'] = edu_form
            return render(request, 'resume-detail.html', context)
        
    if request.method == 'GET':
        edu_form = EducationForm()
        context['edu_form'] = edu_form
        return render(request,  'resume-detail.html', context)
    
    return render(request, 'resume-detail.html', context)