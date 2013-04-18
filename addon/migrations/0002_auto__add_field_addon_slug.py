# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Addon.slug'
        db.add_column(u'addon_addon', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=30, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Addon.slug'
        db.delete_column(u'addon_addon', 'slug')


    models = {
        u'addon.addon': {
            'Meta': {'ordering': "['name']", 'object_name': 'Addon'},
            'config_vars': ('addon.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['addon']