from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

#Signup view function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
         messages.success(request, 'Account banyo hai hajur')
         fm.save()
    else:       
     fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})


#Login view function
def user_login(request):
   if not request.user.is_authenticated:
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST);
        if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          user = authenticate(username=uname, password=upass)
          if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return HttpResponseRedirect('/profile/')
    else:    
      fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html',{'form':fm})
   else:
    return HttpResponseRedirect('/profile/')

# Profile
def user_profile(request):
  if request.user.is_authenticated:
   return render(request, 'enroll/profile.html',{'name': request.user})
  else:
    return HttpResponseRedirect('/login/')
    

#Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')


# change password with old password
def user_change_pass(request):
  if request.user.is_authenticated:
     if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
          fm.save()
          update_session_auth_hash(request, fm.user)
          messages.success(request,'Password changed successfully')
          return HttpResponseRedirect('/profile/')
     else:
      fm = PasswordChangeForm(user=request.user)
     return render(request, 'enroll/changepass.html',{'form':fm})
  else:
    return HttpResponseRedirect('/login/')