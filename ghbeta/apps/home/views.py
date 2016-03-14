from django.shortcuts import render_to_response
from django.template import RequestContext
from ghbeta.apps.realestate.models import Inmueble,Catalogoimg
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):	
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def catalogo_view(request,pagina):
	cat = Catalogoimg.objects.filter(imgportada=True)

	paginator = Paginator(cat,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		catalogo = paginator.page(page)
	except:
		catalogo = paginator.page(paginator.num_pages)
	info = {'catalogo':catalogo}
	return render_to_response('home/catalogo.html',info,context_instance=RequestContext(request))