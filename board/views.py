from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.utils import timezone

from .models import Put
# Create your views here.

def index(request):
    post_list = Put.objects.order_by('-create_date')
    context = {'post_list' : post_list}
    return render(request,'anonym/board_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Put,pk=post_id)
    context = {'post': post}
    return render(request,'anonym/board_detail.html', context)

def input(request):
    return render(request, 'anonym/board_input.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    passwd = request.POST.get('passwd')
    writer = request.POST.get('writer')
    new_post = Put(title=title, content=content, passwd=passwd, writer=writer, create_date=timezone.now())
    new_post.save()
    return redirect('board:detail', post_id=new_post.id)

def delete(request,post_id):
    post = get_object_or_404(Put, pk=post_id)
    post.delete()
    return redirect('board:index')

def editform(request,post_id):
    post = get_object_or_404(Put, pk=post_id)
    context = {'post': post}
    return render(request, 'anonym/board_edit.html', context)


def edit(request, post_id):
    post = get_object_or_404(Put, pk=post_id)

    # 폼에서 전달된 값 가져오기
    title = request.POST.get('title', post.title)  # 기본값으로 기존 title 사용
    content = request.POST.get('profile', post.content)  # 기존 내용 사용
    passwd = request.POST.get('passwd', post.passwd)
    writer = request.POST.get('writer', post.writer)

    # 필드 업데이트
    post.title = title
    post.content = content
    post.passwd = passwd
    post.writer = writer

    # 저장
    post.save()

    return redirect('board:detail', post_id=post.id)

