# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_titledimage.models import *
from django.utils.translation import ugettext as _
from django.contrib import admin

class TitledImagePlugin(CMSPluginBase):
    model = TitledImage
    name = _("Titled Image")
    render_template = "cmsplugin_titledimage/image.html"
    
    def render(self, context, instance, placeholder):
        context.update({'instance' : instance,
        	'template':'cmsplugin_titledimage/image.html'

        	})
        return context

plugin_pool.register_plugin(TitledImagePlugin)