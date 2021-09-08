from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 

# Create your views here.
# def index(request):
#     return render(request, 'pages/blog_home.html')

def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'pages/blog_home.html', Data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'pages/blog_post.html', {'post': post})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})