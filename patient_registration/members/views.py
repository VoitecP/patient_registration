from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View

from .forms import *


class LoginView(View):
    from_class=LoginForm
    template_name='registration/login.html'

    def get(self, request):
        form=self.from_class()
        # message=''
        # context={'form':form,'message':message}
        context={'form':form}
        return render(request,self.template_name,context)
        
    def post(self, request):
        form=self.from_class(request.POST)
        # message=''
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user  is not None :
                login(request, user)
                messages.success(request,("You are logged"))
                return  redirect('base')
            else:
                # message='Login failed'
                messages.success(request,("Error, try again"))
                return redirect('login')
        # context={'form':form,'message':message}
        context={'form':form}
        return render(request, self.template_name,context)

class LogoutView(View):

    def get(self,request):
        logout(request)
        messages.success(request,("You are logged out"))
        return redirect('base')
        
 
class SignupView(View):
    template_name='registration/signup.html'
    
    def get(self,request):
        form=SignupForm() 
        context={'form':form}
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
            
                return redirect('base')
        return render(request,self.template_name, context)