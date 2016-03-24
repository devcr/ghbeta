from django.shortcuts import render_to_response
from django.template import RequestContext
from ghbeta.apps.realestate.models import Inmueble,Catalogoimg
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
	registros = Inmueble.objects.all()[:3] #con esta linea selecciona los primero 10 registros de la tabla de inmuebles
	info = {'registros':registros}
	return render_to_response('home/index.html',info,context_instance=RequestContext(request))

def catalogo_view(request,pagina):
	cat = Inmueble.objects.filter(publicar=True)
	paginator = Paginator(cat,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		catalogo = paginator.page(page)
	except (EmptyPage, InvalidPage):
		catalogo = paginator.page(paginator.num_pages)
	info = {'catalogo':catalogo}
	return render_to_response('home/catalogo.html',info,context_instance=RequestContext(request))

def detalle_view(request,idreg):
	registro	= Inmueble.objects.get(id=idreg)
	imgs		= Catalogoimg.objects.filter(inmueble_id=idreg)
	info = {'registro':registro, 'imgs':imgs}
	return render_to_response('home/detalle.html',info,context_instance=RequestContext(request))

def contacto_view (request):
	return render_to_response('home/contacto.html',context_instance=RequestContext(request))

def filtro_view(request,pagina,categoria,cadfiltro):
	#print "filtro_view()_ cadena filtro: %s"%cadfiltro
	#print "filtro_view()_ cadena categoria: %s"%categoria
	if categoria == "tipoinm":
		qrysel = Inmueble.objects.filter(tipoinmueble=cadfiltro)
	elif categoria == "tipoope":
		qrysel = Inmueble.objects.filter(tipooperacion=cadfiltro)

	paginator = Paginator(qrysel,2)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		registros = paginator.page(page)
	except (EmptyPage, InvalidPage):
		registros = paginator.page(paginator.num_pages)
	info = {'registros':registros,'cadfiltro':cadfiltro,'categoria':categoria}
	return render_to_response('home/filtro.html',info,context_instance=RequestContext(request))

