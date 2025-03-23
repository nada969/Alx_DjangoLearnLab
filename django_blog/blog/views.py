from django.shortcuts import render , redirect 
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()

    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':  
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
            # Authentication failed - form.is_valid() was True but user wasn't found
            # This is rare but could happen if user was deleted after form validation
                form.add_error(None, "Invalid username or password")

    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    pass