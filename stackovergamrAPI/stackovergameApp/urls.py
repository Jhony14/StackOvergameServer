from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import url
from stackovergameApp import views
from django.urls import include, path

from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^tipousuario/$', views.tipousuarioApi),
    url(r'^tipousuario/([0-9]+)$', views.tipousuarioApi),

    url(r'^usuario/$', views.usuarioApi),
    url(r'^usuario/([0-9]+)$', views.usuarioApi),
    url(r'^usuarioAll/$', views.usuarioAllApi),

    url(r'^post/$', views.postApi),
    url(r'^post/([0-9]+)$', views.postApi),
    url(r'^postList/$', views.postListApi),

    url(r'^guide/$', views.guideApi),
    url(r'^guide/([0-9]+)$', views.guideApi),
    url(r'^guideList/$', views.guideListApi),

    url(r'^news/$', views.newsApi),
    url(r'^news/([0-9]+)$', views.newsApi),
    url(r'^newsList/$', views.newsListApi),

    url(r'^comentarios/$', views.comentariosApi),
    url(r'^comentarios/([0-9]+)$', views.comentariosApi),

    url(r'^valoracionpost/$', views.valoracionpostApi),
    url(r'^valoracionpost/([0-9]+)$', views.valoracionpostApi),

    url(r'^valoracioncomentarios/$', views.valoracioncomentariosApi),
    url(r'^valoracioncomentarios/([0-9]+)$', views.valoracioncomentariosApi),

    url(r'^savefile$', views.SaveFile),

    url(r'^accounts/login/$', views.login),
    url(r'^accounts/logout/$', views.logout),

    url(r'^crear/$', views.create_user),

    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
