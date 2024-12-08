from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create a new user instance but don't save to the DB yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the DB

            # Automatically log in the user
            login(request, user)

            return redirect('index')  # Redirect to a home page or dashboard after login
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            return redirect('home')  # Redirect to a list of posts or the newly created post
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

from django.shortcuts import render
from .models import Post

def post_list(request):
    # Retrieve all posts from the database
    posts = Post.objects.all().order_by('-created_at')  # Optionally order by creation date (most recent first)
    return render(request, 'post_list.html', {'posts': posts})



def index(request):
    return render(request,'index.html')
