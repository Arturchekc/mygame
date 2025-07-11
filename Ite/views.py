import os

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from myite import settings
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

def sitemap(request):
    filepath = os.path.join(settings.BASE_DIR, 'Ite', 'static', 'sitemap.xml')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_content = f.read()
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)

    return HttpResponse(xml_content, content_type='application/xml')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))