from django.contrib import admin
from .models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display=["titulo","timestamp","actualizado"]
	list_display_link = ["titulo"]
	list_filter = ["actualizado"]
	#list_editable = ["titulo"] #para editar sin entrar en el link, pero solo funciona si es que lo que se quiere editar no es el mismo link
	search_fields=["titulo","contenido"]
	class Meta:
		model = Post

admin.site.register(Post,PostModelAdmin)