from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from gmaps.models import UbicacionForm

def index(request):
	form = UbicacionForm()
	return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))


def coords_save(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			pass
		else:
			return HttpResponse(simplejson.dumps({'ok': False, 'msg': 'Llena todos los campos'}), mimetype='aplication/json')
