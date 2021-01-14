from django.conf.urls import url
from stackovergameApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^tipousuario/$', views.tipousuarioApi),
    url(r'^tipousuario/([0-9]+)$', views.tipousuarioApi),

    url(r'^usuario/$', views.usuarioApi),
    url(r'^usuario/([0-9]+)$', views.usuarioApi),

    url(r'^post/$', views.postApi),
    url(r'^post/([0-9]+)$', views.postApi),

    url(r'^comentarios/$', views.comentariosApi),
    url(r'^comentarios/([0-9]+)$', views.comentariosApi),

    url(r'^valoracionpost/$', views.valoracionpostApi),
    url(r'^valoracionpost/([0-9]+)$', views.valoracionpostApi),

    url(r'^valoracioncomentarios/$', views.valoracioncomentariosApi),
    url(r'^valoracioncomentarios/([0-9]+)$', views.valoracioncomentariosApi),

    url(r'^savefile$', views.SaveFile),

    url(r'^login/$', views.login),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
