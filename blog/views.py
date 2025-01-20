from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from .models import Post
from .forms import PostForm
from booking.models import Studio, StudioBooking
from users.models import CustomUser, UserProfile

# Create your views here.

#def blog(request):

# Will retrieve all posts from the blog model when its set up
    # post_list = Posts.objects.all() 

#    template = 'blog/blog.html'
#    context = {
#        'blog': blog,
#    }
#    return render(request, template, context)


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(username=request.user)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})    