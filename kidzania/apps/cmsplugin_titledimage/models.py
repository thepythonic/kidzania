# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.files.uploadedfile import SimpleUploadedFile
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField






class TitledImage(CMSPlugin):
    title      = models.CharField(_('title'), max_length=50)
    image      = FilerImageField(null=True, blank=True)
    img_height = models.PositiveSmallIntegerField(_("height"),default='166', editable=True, null=True)
    img_width  = models.PositiveSmallIntegerField(_("width"),default='763', editable=True, null=True)
    alter      = models.TextField(_("Alt text"), blank=True)
    
    def __unicode__(self):
        return self.title

    




   



    
     
    

