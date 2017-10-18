from django.shortcuts import render, get_object_or_404, redirect

from post.forms import PostUploadForm
from post.models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context=context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context=context)


def post_create(request):
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            photo = form.cleaned_data['photo']
            content = form.cleaned_data['content']
            post = Post.objects.create(title=title, photo=photo, content=content)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostUploadForm()
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context=context)
