from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=150)
	contenido = models.TextField()
	timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado=models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id":self.id})

	class Meta:
		ordering = ["-timestamp","-actualizado"]#"-pk" en caso de no tener