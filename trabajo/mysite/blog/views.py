from django.shortcuts import render
from django.utils import timezone
from .models import Vehiculo
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def post_list(request):
    #posts = Vehiculo.objects.filter(fecha_publicacion=timezone.now()).order_by('fecha_publicacion')
    posts = Vehiculo.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=Post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST, instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Vehiculo, pk=pk)
    post.delete()
    return redirect('post_list')

    