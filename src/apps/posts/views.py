from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

#from .models import Post
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	# if request.method == "POST":
	# 	print request.POST.get("titulo")
	# 	print request.POST.get("contenido")
	if form.is_valid():
		instance = form.save(commit=False)
		#commit=False para no guardar de una el form, si es que se quieren hacer algunos cambios antes de guardar en la BD
		print form.cleaned_data.get("titulo")
		instance.save()
		messages.success(request, "El post ha sido creado correctamente")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form,
	}
	return render (request, "post_form.html",context)

def post_detail(request,id=None):
	#hay que definir los parametros que va a recibir, en este caso id=none, none porque toavia no savemos que parametro
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
		"titulo":instance.titulo,
		"instance":instance,
	}
	return render (request, "post_detail.html",context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"titulo":"List",
		"object_list":queryset,
	}
	return render (request, "index.html",context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "El post ha sido modificado correctamente")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"titulo":instance.titulo,
		"instance":instance,
		"form":form,
	}
	return render (request, "post_form.html",context)

def post_delete(request):
	#Este es un tipo de Function views
	return HttpResponse("<h1>Eliminar!</h1>")