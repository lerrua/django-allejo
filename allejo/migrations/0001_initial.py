# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Championship'
        db.create_table(u'allejo_championship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('max_players', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('started_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'allejo', ['Championship'])

        # Adding M2M table for field players on 'Championship'
        m2m_table_name = db.shorten_name(u'allejo_championship_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('championship', models.ForeignKey(orm[u'allejo.championship'], null=False)),
            ('player', models.ForeignKey(orm[u'allejo.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['championship_id', 'player_id'])

        # Adding model 'Player'
        db.create_table(u'allejo_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'allejo', ['Player'])

        # Adding model 'Match'
        db.create_table(u'allejo_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['allejo.Match'])),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_player_set', null=True, to=orm['allejo.Player'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='away_player_set', null=True, to=orm['allejo.Player'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Championship'], null=True, blank=True)),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Player'], null=True, blank=True)),
            ('game_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'allejo', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Championship'
        db.delete_table(u'allejo_championship')

        # Removing M2M table for field players on 'Championship'
        db.delete_table(db.shorten_name(u'allejo_championship_players'))

        # Deleting model 'Player'
        db.delete_table(u'allejo_player')

        # Deleting model 'Match'
        db.delete_table(u'allejo_match')


    models = {
        u'allejo.championship': {
            'Meta': {'object_name': 'Championship'},
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
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Championship']", 'null': 'True', 'blank': 'True'}),
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