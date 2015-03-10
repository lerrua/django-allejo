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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('main_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('main_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'allejo', ['Player'])

        # Adding model 'Match'
        db.create_table(u'allejo_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'home_player_set', to=orm['allejo.Player'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'away_player_set', to=orm['allejo.Player'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Championship'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Player'], null=True, blank=True)),
            ('game_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=1, null=True, blank=True)),
            ('turn', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=1, null=True, blank=True)),
            ('main_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'allejo', ['Match'])

        # Adding model 'Standings'
        db.create_table(u'allejo_standings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['allejo.Championship'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'player_set', to=orm['allejo.Player'])),
            ('category', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=1, null=True, blank=True)),
            ('turn', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=1, null=True, blank=True)),
            ('games_played', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('draws', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goals_for', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goals_against', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goals_difference', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'allejo', ['Standings'])


    def backwards(self, orm):
        # Deleting model 'Championship'
        db.delete_table(u'allejo_championship')

        # Removing M2M table for field players on 'Championship'
        db.delete_table(db.shorten_name(u'allejo_championship_players'))

        # Deleting model 'Player'
        db.delete_table(u'allejo_player')

        # Deleting model 'Match'
        db.delete_table(u'allejo_match')

        # Deleting model 'Standings'
        db.delete_table(u'allejo_standings')


    models = {
        u'allejo.championship': {
            'Meta': {'object_name': 'Championship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'max_players': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['allejo.Player']", 'symmetrical': 'False'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'allejo.match': {
            'Meta': {'object_name': 'Match'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'away_player_set'", 'to': u"orm['allejo.Player']"}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Championship']"}),
            'game_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'home_player_set'", 'to': u"orm['allejo.Player']"}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'turn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Player']", 'null': 'True', 'blank': 'True'})
        },
        u'allejo.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        },
        u'allejo.standings': {
            'Meta': {'object_name': 'Standings'},
            'category': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['allejo.Championship']"}),
            'draws': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'games_played': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goals_against': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goals_difference': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goals_for': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'player_set'", 'to': u"orm['allejo.Player']"}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'turn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['allejo']