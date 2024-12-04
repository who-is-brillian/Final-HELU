from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Post
from django.contrib.auth.decorators import login_required

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'forum/topic_list.html', {'topics': topics})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'forum/topic_detail.html', {'topic': topic})

@login_required
def new_topic(request):
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
    return render(request, 'forum/new_post.html', {'topic': topic})
