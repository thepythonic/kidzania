# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.files.uploadedfile import SimpleUploadedFile
from cms.models.pluginmodel import CMSPlugin
from filer.fields.folder import FilerFolderField

from PIL import Image
from cStringIO import StringIO

DEF_SIZE = (800, 600)

TEMPLATE_CHOICE = (
        ("", _("--select--")),
        ("banner-carousel.html", "default"),
        ("brands-carousel.html", "brands carousel"),
        )



class Carousel(CMSPlugin):
    domid = models.CharField(_('Domid'), max_length=50)
    interval = models.IntegerField(_('Interval'), default=5000)
    album = FilerFolderField(verbose_name=_('album'))
    template = models.CharField(max_length=50, default='banner-carousel.html', choices=TEMPLATE_CHOICE)
    
    @property
    def images(self):
        if not hasattr(self, '__images'):
            files = self.album.files.order_by('name', 'original_filename')
            self.__images = [f for f in files if f.file_type == 'Image']
        return self.__images
    
    def __unicode__(self):
        return self.domid

    
    
     
    

