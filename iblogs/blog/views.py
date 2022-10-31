from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django import forms
from django.forms import inlineformset_factory
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import *
from blog.forms import PostsModelForm,CategoryModelForm
from .forms import CommentForm


# Create your views here.
def welcome(request):
    return render(request,"welcome.html")



def registerPage(request):
    #if request.user.is_authenticated:
       # return redirect('home')
    #else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

            return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
   # if request.user.is_authenticated:
      #  return redirect('home')
   # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
               login(request, user)
               return redirect('home')
            messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})

class AddCommentView(CreateView):
    model = Comment
    #form_class = CommentForm
    template_name = 'add_comment.html'
    fields ='__all__'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

class AddPostView(CreateView):
    form_class = PostsModelForm
    template_name = "add_post.html"
    extra_context = {'title': "Add New Post"}
    success_url = '../home'
class AddCategoryView(CreateView):
    form_class = CategoryModelForm
    template_name = "add_category.html"
    extra_context = {'title': "Add New Post"}
    success_url = '../home'



def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})

def BlogPostLike(request, url):
    post = get_object_or_404(BlogPost, id=request.POST.get('post'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))
class BlogPostDetailView(DetailView):
    model = BlogPost
     #template = 'iblogs/BlogPost_detail.html'
     #context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return render(request, 'template/BlogPost_detail.html', data)



