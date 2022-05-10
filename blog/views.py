from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.
#def index(request):
#    posts=Post.objects.all()
#
#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts': posts,
#        }
#    )

class PostList(ListView):
    model =Post
    ordering='-pk'

class PostDetail(DetailView):
    model=Post




# Post.object.get에 pk대입 ->같은 값을 가져오는 의미 값이 html에 렌더링
def single_post_page(request,pk):
    post=Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )    