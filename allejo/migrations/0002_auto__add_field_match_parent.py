# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Match.parent'
        db.add_column(u'allejo_match', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['allejo.Match']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Match.parent'
        db.delete_column(u'allejo_match', 'parent_id')


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
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['allejo.Match']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Player']", 'null': 'True', 'blank': 'True'})
        },
        u'allejo.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['allejo']