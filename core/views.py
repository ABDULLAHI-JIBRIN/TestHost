from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.views import generic
# Create your views here.


def home(request):
    posts = Post.objects.order_by('date')[:]
    context = {
        'posts':posts
    }
    return render(request, 'core/home.html', context)



def post_detail_view(request,id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post':post
    }

    return render(request, 'core/post_detail.html',context)



class   CreatePost(generic.CreateView):
    
    model = Post
    template_name = 'core/create_post.html'
    fields = [
        'title','content','category','is_complete'
    ]


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)





