# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'qa_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='question_author', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'qa', ['Question'])

        # Adding M2M table for field likes on 'Question'
        db.create_table(u'qa_question_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'qa.question'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'qa_question_likes', ['question_id', 'user_id'])

        # Adding model 'Answer'
        db.create_table(u'qa_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qa.Question'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'qa', ['Answer'])

        # Adding model 'Author'
        db.create_table(u'qa_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'qa', ['Author'])

        # Adding model 'Article'
        db.create_table(u'qa_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qa.Author'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('descr', self.gf('django.db.models.fields.TextField')(default='adsf')),
        ))
        db.send_create_signal(u'qa', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'qa_question')

        # Removing M2M table for field likes on 'Question'
        db.delete_table('qa_question_likes')

        # Deleting model 'Answer'
        db.delete_table(u'qa_answer')

        # Deleting model 'Author'
        db.delete_table(u'qa_author')

        # Deleting model 'Article'
        db.delete_table(u'qa_article')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'qa.answer': {
            'Meta': {'object_name': 'Answer'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qa.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'qa.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qa.Author']"}),
            'descr': ('django.db.models.fields.TextField', [], {'default': "'adsf'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'qa.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'qa.question': {
            'Meta': {'object_name': 'Question'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_author'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'question_like'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['qa']