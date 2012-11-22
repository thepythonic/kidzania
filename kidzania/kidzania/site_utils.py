from django.template.loader import render_to_string 
from django.http import HttpResponseNotFound, HttpResponseServerError
from cms.views import details 
from cms.models import Title,Page


def handler404(request):
	title = Title.objects.get(slug='page-not-found').page
	page = Page.get_template(title)
	return HttpResponseNotFound(render_to_string(page))

def handler500(request):
	title = Title.objects.get(slug='internal-server-error').page
	page = Page.get_template(title)
	return HttpResponseServerError(render_to_string(page))
