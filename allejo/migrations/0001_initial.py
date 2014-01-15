# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Champioship'
        db.create_table(u'allejo_champioship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('max_players', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('started_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'allejo', ['Champioship'])

        # Adding M2M table for field players on 'Champioship'
        m2m_table_name = db.shorten_name(u'allejo_champioship_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('champioship', models.ForeignKey(orm[u'allejo.champioship'], null=False)),
            ('player', models.ForeignKey(orm[u'allejo.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['champioship_id', 'player_id'])

        # Adding model 'Player'
        db.create_table(u'allejo_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'allejo', ['Player'])

        # Adding model 'Match'
        db.create_table(u'allejo_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_player_set', null=True, to=orm['allejo.Player'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='away_player_set', null=True, to=orm['allejo.Player'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('champioship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Champioship'], null=True, blank=True)),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Player'], null=True, blank=True)),
            ('game_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'allejo', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Champioship'
        db.delete_table(u'allejo_champioship')

        # Removing M2M table for field players on 'Champioship'
        db.delete_table(db.shorten_name(u'allejo_champioship_players'))

        # Deleting model 'Player'
        db.delete_table(u'allejo_player')

        # Deleting model 'Match'
        db.delete_table(u'allejo_match')


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
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Player']", 'null': 'True', 'blank': 'True'})
        },
        u'allejo.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['allejo']