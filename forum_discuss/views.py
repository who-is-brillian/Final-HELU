from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Post
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TopicForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

def topic_list(request):
    topics = Topic.objects.all()
    latest_topics = Topic.objects.order_by('-created_at')[:5]  # Ambil 5 topik terbaru
    popular_topics = Topic.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:5]  # Ambil 5 topik populer

    context = {
        'topics': topics,
        'latest_topics': latest_topics,
        'popular_topics': popular_topics,
        'view': 'topic_list',
    }

    if request.method == 'POST' and request.user.is_authenticated:
        topic_id = request.POST.get('topic_id')
        content = request.POST.get('content')
        if content:
            topic = get_object_or_404(Topic, id=topic_id)
            Post.objects.create(topic=topic, content=content, created_by=request.user)
            return redirect('.')  # Refresh halaman
        else:
            context['error_message'] = "Konten balasan harus diisi."

    return render(request, 'forum/index.html', context)

@login_required
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = Post.objects.filter(topic=topic, parent=None).order_by('created_at')  # Hanya post utama

    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')  # Ambil ID parent jika ada
        parent = Post.objects.filter(id=parent_id).first() if parent_id else None

        if content:
            Post.objects.create(
                topic=topic,
                content=content,
                parent=parent,
                created_by=request.user
            )
            return redirect('topic_detail', pk=pk)
        else:
            context = {'topic': topic, 'posts': posts, 'error_message': "Konten balasan harus diisi."}
            return render(request, 'forum/index.html', context)

    context = {'topic': topic, 'posts': posts, 'view': 'topic_detail'}
    return render(request, 'forum/index.html', context)


@login_required
def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(topic=topic, content=content, created_by=request.user)
            return redirect('topic_detail', pk=pk)
        else:
            context = {'topic': topic, 'error_message': "Konten balasan harus diisi.", 'view': 'new_post'}
            return render(request, 'forum/index.html', context)
    context = {'topic': topic, 'view': 'new_post'}
    return render(request, 'forum/index.html', context)


@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)  # Tambahkan request.FILES
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            return redirect('topic_list')
        else:
            context = {'form': form, 'view': 'new_topic'}
            return render(request, 'forum/new_topic.html', context)
    else:
        form = TopicForm()
    context = {'form': form, 'view': 'new_topic'}
    return render(request, 'forum/new_topic.html', context)



@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.created_by or request.user.is_staff:
        post.delete()
        return redirect('topic_detail', pk=post.topic.pk)  # Ganti dengan nama URL detail topik Anda
    return HttpResponseForbidden("Anda tidak memiliki izin untuk menghapus komentar ini.")


@login_required
def delete_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.user != topic.created_by and not request.user.is_staff:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menghapus topik ini.")
    
    if request.method == 'POST':  # Konfirmasi penghapusan
        topic.delete()
        return redirect('topic_list')
    
    return render(request, 'forum/confirm_delete.html', {'topic': topic})

@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(Post, pk=pk)
    if request.user != reply.created_by and not request.user.is_staff:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menghapus balasan ini.")

    if request.method == 'POST':
        topic_pk = reply.topic.pk
        reply.delete()
        return redirect('topic_detail', pk=topic_pk)

    return render(request, 'forum/confirm_delete.html', {'post': reply})


def get_referer_url(request):
    """Helper to get the referer URL or fallback to a default."""
    return request.META.get('HTTP_REFERER', '/')

@login_required
def like_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.user in topic.likes.all():
        topic.likes.remove(request.user)  # Jika sudah like, maka hapus like
    else:
        topic.likes.add(request.user)  # Tambahkan like
        topic.unlikes.remove(request.user)  # Pastikan unlike dihapus jika ada
    return redirect(get_referer_url(request))

@login_required
def unlike_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.user in topic.unlikes.all():
        topic.unlikes.remove(request.user)  # Jika sudah unlike, maka hapus unlike
    else:
        topic.unlikes.add(request.user)  # Tambahkan unlike
        topic.likes.remove(request.user)  # Pastikan like dihapus jika ada
    return redirect(get_referer_url(request))


@login_required
def edit_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.user != topic.created_by and not request.user.is_staff:
        return redirect('topic_list')
    
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=topic)  # Tambahkan request.FILES
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm(instance=topic)
    
    context = {'form': form, 'topic': topic, 'view': 'edit_topic'}
    return render(request, 'forum/edit_topic.html', context)

def find_topic(request):
    query = request.GET.get('q', '')  # Ambil input pencarian
    topics = Topic.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-created_at')  # Filter berdasarkan judul atau deskripsi
    paginator = Paginator(topics, 10)  # Batasi 10 topik per halaman
    page_number = request.GET.get('page', 1)
    page_topics = paginator.get_page(page_number)

    context = {
        'topics': page_topics,
        'query': query,
    }
    return render(request, 'forum/find_topic.html', context)

def custom_404_view(request, exception=None):
    return render(request, 'errors/404.html', status=404)

