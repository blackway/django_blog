# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Board'
        db.create_table(u'blog_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Board'])


    def backwards(self, orm):
        # Deleting model 'Board'
        db.delete_table(u'blog_board')


    models = {
        u'blog.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']