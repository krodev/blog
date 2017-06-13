from django.conf.urls import include,url
from . import views
#solo . porque es una importacion relativa, esta en la misma carpeta
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail,name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
#ordenar las url
]
