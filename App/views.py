from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.views import View,generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        comments = post.comments.filter(active=True)
        comment_form = CommentForm()
        return render(request, self.template_name, {
            'object': post,
            'comments': comments,
            'comment_form': comment_form
        })

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        comments = post.comments.filter(active=True)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
        return render(request, self.template_name, {
            'object': post,
            'comments': comments,
            'comment_form': comment_form
        })

def reports(request):
    return render(request, 'reports.html')

def policy(request):
    return render(request, 'policy.html')

def upvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.upvotes += 1
    post.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def clap_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.claps += 1
    post.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

