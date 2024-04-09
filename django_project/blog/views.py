from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post, Project


@login_required
def delete_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    context = {"post": post}

    if request.method == "GET":
        return render(request, "blog/post_confirm_delete.html", context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted successfully.")
        return redirect("posts")


@login_required
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)

    if request.method == "GET":
        context = {"form": PostForm(instance=post), "id": id}
        return render(request, "blog/post_form.html", context)

    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been updated successfully.")
            return redirect("posts")
        else:
            messages.error(request, "Please correct the following errors:")
            return render(request, "blog/post_form.html", {"form": form})


@login_required
def create_post(request):
    if request.method == "GET":
        context = {"form": PostForm()}
        return render(request, "blog/post_form.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("posts")
        else:
            messages.error(request, "Please correct the following errors:")
            return render(request, "blog/post_form.html", {"form": form})

# https://realpython.com/django-social-forms-4/
def home(request, project_id=0):
    id = -1
    if request.method == "POST":
        form = 
        posts = Post.objects.all()
        print(request.POST)
    else:
        posts = Post.objects.all()
        # posts = get_object_or_404(Post)
    print(f"project_id={project_id} / {id}")
    # if project_id > 0:
    #     projects = Project.objects.get(pk=project_id)
    # else:
    projects = Project.objects.all().order_by("name")
    print(projects)
    context = {"posts": posts, "projects": projects}
    return render(request, "blog/home.html", context)
