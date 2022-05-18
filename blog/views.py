from unicodedata import category
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from .models import Post,Category

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
    ordering='pk'

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context


def category_page(request,slug):
    if slug == 'no_category':
        category='미분류'
        post_list = Post.objects.filter(category =None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category = category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories':Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category':category,
        }
    )    

class PostDetail(DetailView):
    model=Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context




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