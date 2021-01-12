from django.conf.urls import url
from stackovergameApp import views

urlpatterns = [
    url(r'^tipousuario/$', views.tipousuarioApi),
    url(r'^tipousuario/([0-9]+)$', views.tipousuarioApi),

    url(r'^usuario/$', views.usuarioApi),
    url(r'^usuario/([0-9]+)$', views.usuarioApi)
]
