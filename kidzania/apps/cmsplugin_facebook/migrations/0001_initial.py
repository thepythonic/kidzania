# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookLikeBox'
        db.create_table('cmsplugin_facebooklikebox', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=587)),
            ('connections', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=10)),
            ('transparent', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('stream', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('header', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('cmsplugin_facebook', ['FacebookLikeBox'])

        # Adding model 'FacebookLikeButton'
        db.create_table('cmsplugin_facebooklikebutton', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='standard', max_length=50)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=80)),
            ('verb', self.gf('django.db.models.fields.CharField')(default='like', max_length=50)),
            ('font', self.gf('django.db.models.fields.CharField')(default='verdana', max_length=50)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
        ))
        db.send_create_signal('cmsplugin_facebook', ['FacebookLikeButton'])


    def backwards(self, orm):
        # Deleting model 'FacebookLikeBox'
        db.delete_table('cmsplugin_facebooklikebox')

        # Deleting model 'FacebookLikeButton'
        db.delete_table('cmsplugin_facebooklikebutton')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_facebook.facebooklikebox': {
            'Meta': {'object_name': 'FacebookLikeBox', 'db_table': "'cmsplugin_facebooklikebox'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'connections': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '587'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'transparent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cmsplugin_facebook.facebooklikebutton': {
            'Meta': {'object_name': 'FacebookLikeButton', 'db_table': "'cmsplugin_facebooklikebutton'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'verdana'", 'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '80'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'verb': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_facebook']