from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.utils.timesince import timesince
from gmaps.models import UbicacionForm, Ubicacion

def index(request):
	form = UbicacionForm()
	Ubicaciones = Ubicacion.objects.all().order_by('-fecha')
	return render_to_response('index.html', {'form': form, 'Ubicaciones': Ubicaciones}, context_instance=RequestContext(request))


def coords_save(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			Ubicaciones = Ubicacion.objects.all().order_by('-fecha')

			data = '<ul id="ubicaciones">'
			for ubicacion in Ubicaciones:
				data += '<li> %s %s - hace %s </li>' % (ubicacion.nombre, ubicacion.user, timesince(ubicacion.fecha))

			data += '</ul>'

			return HttpResponse(simplejson.dumps({'ok': True, 'msg': data}), mimetype="aplication/json")
		else:
			return HttpResponse(simplejson.dumps({'ok': False, 'msg': 'Llena todos los campos'}), mimetype='aplication/json')
