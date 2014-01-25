# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Board.created_at'
        db.add_column(u'blog_board', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 1, 23, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Board.created_at'
        db.delete_column(u'blog_board', 'created_at')


    models = {
        u'blog.board': {
            'Meta': {'object_name': 'Board'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']