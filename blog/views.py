from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Post
from . forms import PostForm
from django.contrib import messages


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
    
def add_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'POST added')
            return redirect('/addblog')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify you blog field')
            return render(request,'blog/addblog.html',{
                'form':form
            })
        
    context = {
        'form': PostForm
    }
    return render(request, 'blog/addblog.html', context)

