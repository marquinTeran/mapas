from django.shortcuts import render_to_response
from django.template import RequestContext
from gmaps.models import UbicacionForm

def index(request):
	form = UbicacionForm()
	return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))