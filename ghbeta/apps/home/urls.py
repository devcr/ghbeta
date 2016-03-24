from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ghbeta.apps.home.views',
	url(r'^$','index_view',name='index_vista'),
	url(r'^catalogo/page/(?P<pagina>.*)/$','catalogo_view',name='catalogo_vista'),
	url(r'^detalle/registro/(?P<idreg>.*)/$','detalle_view',name='detalle_vista'),
	url(r'^contacto/$','contacto_view',name='contacto_vista'),
	#url(r'^filtro/page/(?P<pagina>.*)/(?P<cadfiltro>.*)/$','filtro_view',name='filtro_vista'),
	url(r'^filtro/page/(?P<pagina>.*)/(?P<categoria>.*)/(?P<cadfiltro>.*)/$','filtro_view',name='filtro_vista'),
	)