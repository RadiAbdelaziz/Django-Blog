from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm , CommentForm

# Create your views here.
from .models import Post 

from django.http import HttpResponse

def show_all_post(req) :
    all_post = Post.objects.all()
    return render(req , "blog/show_post.html" , {"posts" : all_post})


def post_details(req , pr):
    post = Post.objects.get(id=pr)
    comments = post.comments.all().order_by("created_at")
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = req.user
            comment.save()
            return redirect("post_details" ,pr=post.id)
    else :
        form = CommentForm()
        
    return render(req , "blog/post_details.html" , {"post" : post , "form" :CommentForm , "comments" : comments})



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(id = 1)
            form.save()
            return redirect('show_post') 
    else:
        form = PostForm()
    
    return render(request, 'blog\create_post.html', {'form': form})



def delete_post(req , pr):
    post = Post.objects.get(id=pr)
    post.delete()
    return redirect("show_post")


def home_page(req):
    return render(req , 'blog\home_page.html')
