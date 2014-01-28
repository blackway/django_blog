# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Picture.image'
        db.delete_column(u'picture_picture', 'image')

        # Adding field 'Picture.file'
        db.add_column(u'picture_picture', 'file',
                      self.gf('django.db.models.fields.files.FileField')(default=datetime.datetime(2014, 1, 24, 0, 0), max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Picture.image'
        db.add_column(u'picture_picture', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 1, 24, 0, 0), max_length=100),
                      keep_default=False)

        # Deleting field 'Picture.file'
        db.delete_column(u'picture_picture', 'file')


    models = {
        u'picture.picture': {
            'Meta': {'object_name': 'Picture'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['picture']