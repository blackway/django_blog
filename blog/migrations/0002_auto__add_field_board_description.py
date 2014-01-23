# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Board.description'
        db.add_column(u'blog_board', 'description',
                      self.gf('django.db.models.fields.TextField')(default=u'', max_length=2000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Board.description'
        db.delete_column(u'blog_board', 'description')


    models = {
        u'blog.board': {
            'Meta': {'object_name': 'Board'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']