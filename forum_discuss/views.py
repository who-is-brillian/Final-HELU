from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def topic_list(request):
    topics = Topic.objects.all()
    if request.method == 'POST' and request.user.is_authenticated:
        topic_id = request.POST.get('topic_id')
        content = request.POST.get('content')
        if topic_id and content:
            topic = get_object_or_404(Topic, pk=topic_id)
            Post.objects.create(
                topic=topic, 
                content=content, 
                created_by=request.user
            )
        return redirect('topic_list')
    return render(request, 'forum/topic_list.html', {'topics': topics})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'forum/topic_detail.html', {'topic': topic})


@login_required
def new_topic(request):
    if not request.user.is_staff:  # Memeriksa apakah pengguna adalah admin/staf
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menambahkan topik.")

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        topic = Topic.objects.create(
            title=title, 
            description=description, 
            created_by=request.user
        )
        return redirect('topic_detail', pk=topic.pk)

    return render(request, 'forum/new_topic.html')


@login_required
def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        content = request.POST['content']
        Post.objects.create(
            topic=topic, 
            content=content, 
            created_by=request.user
        )
        return redirect('topic_detail', pk=topic.pk)
    return render(request, 'forum/topic_list.html', {'topic': topic})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.created_by and not request.user.is_staff:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menghapus komentar ini.")

    if request.method == 'POST':  # Jika pengguna mengonfirmasi penghapusan
        topic_pk = post.topic.pk
        post.delete()
        return redirect('topic_detail', pk=topic_pk)

    return render(request, 'forum/confirm_delete.html', {'post': post})



