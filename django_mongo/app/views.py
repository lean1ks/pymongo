from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list_of_posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if 'update' in request.POST:
            post.title_news = request.POST.get('title')
            post.category = request.POST.get('category')
            post.data = request.POST.get('data')
            post.url_img = request.POST.get('url_img')
            post.save()
        elif 'delete' in request.POST:
            post.delete()
            return redirect('post_list')
    return render(request, 'detail_or_delete.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title_news = request.POST.get('title_news')
        category = request.POST.get('category')
        data = request.POST.get('data')
        url_img = request.POST.get('url_img')
        last_post = Post.objects.order_by('-id').first()
        new_post_id = last_post.id + 1 if last_post else 1
        Post.objects.create(
            id=new_post_id,
            title_news=title_news, 
            category=category,
            data=data,
            url_img=url_img
        )
        return redirect('post_list')
    return render(request, 'create_post.html')