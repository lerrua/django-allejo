# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Match.lft'
        db.add_column(u'allejo_match', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Match.rght'
        db.add_column(u'allejo_match', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Match.tree_id'
        db.add_column(u'allejo_match', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Match.level'
        db.add_column(u'allejo_match', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Match.lft'
        db.delete_column(u'allejo_match', u'lft')

        # Deleting field 'Match.rght'
        db.delete_column(u'allejo_match', u'rght')

        # Deleting field 'Match.tree_id'
        db.delete_column(u'allejo_match', u'tree_id')

        # Deleting field 'Match.level'
        db.delete_column(u'allejo_match', u'level')


    models = {
        u'allejo.champioship': {
            'Meta': {'object_name': 'Champioship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_players': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['allejo.Player']", 'symmetrical': 'False'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'allejo.match': {
            'Meta': {'object_name': 'Match'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'away_player_set'", 'null': 'True', 'to': u"orm['allejo.Player']"}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'champioship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Champioship']", 'null': 'True', 'blank': 'True'}),
            'game_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_player_set'", 'null': 'True', 'to': u"orm['allejo.Player']"}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['allejo.Match']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Player']", 'null': 'True', 'blank': 'True'})
        },
        u'allejo.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['allejo']