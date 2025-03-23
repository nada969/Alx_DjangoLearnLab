from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
"Post.objects.filter", "title__icontains", "tags__name__icontains", "content__icontains"
# ListView to display all blog posts.
# DetailView to show individual blog posts.
# CreateView to allow authenticated users to create new posts.
# UpdateView to enable post authors to edit their posts.
# DeleteView to let authors delete their posts.

class post_view(ListView):
    template_name = 'posts/post.html'
    model = Post

class create_post(LoginRequiredMixin,CreateView):
    template_name = 'posts/create_post.html'
    model = Post
    
    def get_success_url(self):
        return reverse('post')

class post_detail(DeleteView):
    template_name = 'posts/create_post.html'
    model = Post

class post_delete(DeleteView):
    template_name = 'posts/create_post.html'
    model = Post

class post_update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = 'posts/create_post.html'
    model = Post


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

    return render(request,'blog/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':  
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)

            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
            # Authentication failed - form.is_valid() was True but user wasn't found
            # This is rare but could happen if user was deleted after form validation
                form.add_error(None, "Invalid username or password")

    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    pass

def profile(request,username):
    if request.method == "GET":
        user = get_object_or_404(User, username=username)

    return render(request, 'blog/profile.html', {'user': user})
