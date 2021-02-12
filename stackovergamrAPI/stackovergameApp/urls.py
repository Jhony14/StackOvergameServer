from django.conf.urls import url
from stackovergameApp import views

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^tipousuario/$', views.tipousuarioApi),
    url(r'^tipousuario/([0-9]+)$', views.tipousuarioApi),

    url(r'^usuario/$', views.usuarioApi),
    url(r'^usuario/([0-9]+)$', views.usuarioApi),

    url(r'^usuarioAll/$', views.usuarioAllApi),

    url(r'^post/$', views.postApi),
    url(r'^post/([0-9]+)$', views.postApi),

    url(r'^postList/$', views.postListApi),

    url(r'^comentarios/$', views.comentariosApi),
    url(r'^comentarios/([0-9]+)$', views.comentariosApi),

    url(r'^valoracionpost/$', views.valoracionpostApi),
    url(r'^valoracionpost/([0-9]+)$', views.valoracionpostApi),

    url(r'^valoracioncomentarios/$', views.valoracioncomentariosApi),
    url(r'^valoracioncomentarios/([0-9]+)$', views.valoracioncomentariosApi),

    url(r'^savefile$', views.SaveFile),

    url(r'^accounts/login/$', views.login),
    url(r'^accounts/logout/$', views.logout),

    url(r'^crear/$', views.signup),

    url(r'^prueba/$', views.prueba),

    #  url(r'^createuser/$', views.UserCreateAPIView),

    # url(r'^register/$', views.register),

    # url(r'^create/$', views.create),
    # url(r'^singup/$', views.signup),

    # url(r'^check/$', views.check),

    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
