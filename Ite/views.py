from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Comment

def index(request):
    comments = Comment.objects.order_by('-created_at')
    return render(request, 'home.html', {'comments': comments})

def about(request):
    comments = Comment.objects.order_by('-created_at')
    if request.user.is_authenticated:
        return render(request, 'secret.html', {'comments': comments})
    else:
        return render(request, 'about.html', {'comments': comments})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('secret')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def secret_page(request):
    comments = Comment.objects.order_by('-created_at')
    return render(request, 'secret.html', {'comments': comments})

@require_POST
@login_required
def post_comment(request):
    content = request.POST.get('comment')
    if content:
        Comment.objects.create(user=request.user, content=content)
    return redirect(request.META.get('HTTP_REFERER', '/'))