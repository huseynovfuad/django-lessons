from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/accounts/login/")
def index_view(request):
    blogs = Blog.objects.order_by("-created_at")

    if request.method == "POST":
        print(request.POST)

    context = {
        "blogs": blogs
    }
    return render(request, "index.html", context)


def create_view(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            new_blog = form.save()
            return redirect("blogs:index")

    context = {
        "form": form
    }
    return render(request, "create.html", context)