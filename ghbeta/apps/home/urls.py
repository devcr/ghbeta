from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ghbeta.apps.home.views',
	url(r'^$','index_view',name='vista_index'),
	url(r'^catalogo/page/(?P<pagina>.*)/$','catalogo_view',name='catalogo_vista'),
	)