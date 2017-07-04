from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify


class PostManager(models.Manager):
	#Post.objects.all()
	#Post.objects.create()
	def active(self,*args,**kwargs):
		#esto sobreescribe el .all()
		return super(PostManager,self).filter(draf=False).filter(publish__lte=timezone.now())

# Create your models here.
def upload_location(instance,filename):
	return "%s/%s"%(instance.id,filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	titulo = models.CharField(max_length=150)
	slug = models.SlugField(unique=True) #slug es un nombre de link personalizado#
	imagen = models.ImageField(upload_to=upload_location,
		null=True, blank=True, 
		height_field='height_field', 
		width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	contenido = models.TextField()
	draf = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado=models.DateTimeField(auto_now_add=False, auto_now=True)

	objects = PostManager()

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"slug":self.slug})

	class Meta:
		ordering = ["-timestamp","-actualizado"]#"-pk" en caso de no tener

#funcion recursiva para buscar/crear un slug,  e importar de utils slugigy
#esto va a crear un slug si es que el post no tiene un slug todavia
def create_slug(instance, new_slug=None):
	slug= slugify(instance.titulo)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")#para verificar si ya existe, tiene qu ser unico
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args,**kwargs): #senal
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)