# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('main_image', models.ImageField(null=True, upload_to='allejo/championship', blank=True)),
                ('max_players', models.PositiveIntegerField(verbose_name='Max of players')),
                ('started_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Championship',
                'verbose_name_plural': 'Championships',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_score', models.IntegerField(null=True, verbose_name='Score home player', blank=True)),
                ('away_score', models.IntegerField(null=True, verbose_name='Score away player', blank=True)),
                ('game_date', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('category', models.CharField(max_length=100, blank=True, help_text='Example: playoffs, final, quarter-final', null=True, verbose_name='Category', db_index=True)),
                ('group', models.CharField(max_length=1, blank=True, help_text='Example: A, B, C, D', null=True, verbose_name='Group', db_index=True)),
                ('turn', models.CharField(max_length=1, blank=True, help_text='Example: 1, 2', null=True, verbose_name='Turn', db_index=True)),
                ('main_image', models.ImageField(null=True, upload_to='allejo/match', blank=True)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name', db_index=True)),
                ('main_image', models.ImageField(null=True, upload_to='allejo/player', blank=True)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, blank=True, help_text='Example: playoffs, final, quarter-final', null=True, verbose_name='Category', db_index=True)),
                ('group', models.CharField(max_length=1, blank=True, help_text='Example: A, B, C, D', null=True, verbose_name='Group', db_index=True)),
                ('turn', models.CharField(max_length=1, blank=True, help_text='Example: 1, 2', null=True, verbose_name='Turn', db_index=True)),
                ('games_played', models.IntegerField(default=0, verbose_name='Games Played')),
                ('points', models.IntegerField(default=0, verbose_name='Points')),
                ('wins', models.IntegerField(default=0, verbose_name='Wins')),
                ('draws', models.IntegerField(default=0, verbose_name='Draws')),
                ('losses', models.IntegerField(default=0, verbose_name='Losses')),
                ('goals_for', models.IntegerField(default=0, verbose_name='Goals For')),
                ('goals_against', models.IntegerField(default=0, verbose_name='Goals Against')),
                ('goals_difference', models.IntegerField(default=0, verbose_name='Goals Difference')),
                ('championship', models.ForeignKey(verbose_name='Championship', to='allejo.Championship')),
                ('player', models.ForeignKey(related_name='player_set', verbose_name='Player', to='allejo.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='away',
            field=models.ForeignKey(related_name='away_player_set', verbose_name='Away player', to='allejo.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='championship',
            field=models.ForeignKey(verbose_name='Choice a championship', to='allejo.Championship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='home',
            field=models.ForeignKey(related_name='home_player_set', verbose_name='Home player', to='allejo.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(verbose_name='Player winner', blank=True, to='allejo.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='championship',
            name='players',
            field=models.ManyToManyField(to='allejo.Player', verbose_name='Players'),
            preserve_default=True,
        ),
    ]
