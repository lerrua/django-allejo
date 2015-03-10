# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Championship(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200)

    main_image = models.ImageField(
        upload_to='allejo/championship', blank=True, null=True)

    max_players = models.PositiveIntegerField(
        verbose_name=_('Max of players'))

    players = models.ManyToManyField(
        'Player', verbose_name=_('Players')
    )

    started_at = models.DateTimeField()

    class Meta:
        verbose_name = _('Championship')
        verbose_name_plural = _('Championships')

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(
        verbose_name=_('Name'), max_length=200, db_index=True)

    main_image = models.ImageField(
        upload_to='allejo/player', blank=True, null=True)

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

    def __unicode__(self):
        return self.name


class Match(models.Model):
    home = models.ForeignKey(
        'Player',
        verbose_name=_('Home player'),
        related_name='home_player_set'
    )

    home_score = models.IntegerField(
        verbose_name=_('Score home player'), blank=True, null=True
    )

    away = models.ForeignKey(
        'Player',
        verbose_name=_('Away player'),
        related_name='away_player_set')

    away_score = models.IntegerField(
        verbose_name=_('Score away player'), blank=True, null=True)

    championship = models.ForeignKey(
        'Championship',
        verbose_name=_('Choice a championship')
    )

    winner = models.ForeignKey(
        'Player',
        verbose_name=_('Player winner'),
        blank=True, null=True
    )

    game_date = models.DateTimeField(blank=True, null=True)

    location = models.CharField(
        verbose_name=_('Location'), max_length=200)

    category = models.CharField(
        verbose_name=_('Category'), max_length=100,
        blank=True, null=True, db_index=True,
        help_text=_('Example: playoffs, final, quarter-final')
    )

    group = models.CharField(
        verbose_name=_('Group'), max_length=1,
        blank=True, null=True, db_index=True,
        help_text=_('Example: A, B, C, D')
    )

    turn = models.CharField(
        verbose_name=_('Turn'), max_length=1,
        blank=True, null=True, db_index=True,
        help_text=_('Example: 1, 2')
    )

    main_image = models.ImageField(
        upload_to='allejo/match', blank=True, null=True)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        return "%s %s - %s" % (self.championship.name, self.home, self.away)


class Standings(models.Model):
    championship = models.ForeignKey(
        'Championship',
        verbose_name=_('Championship')
    )

    player = models.ForeignKey(
        'Player',
        verbose_name=_('Player'),
        related_name='player_set'
    )

    category = models.CharField(
        verbose_name=_('Category'), max_length=100,
        blank=True, null=True, db_index=True,
        help_text=_('Example: playoffs, final, quarter-final')
    )

    group = models.CharField(
        verbose_name=_('Group'), max_length=1,
        blank=True, null=True, db_index=True,
        help_text=_('Example: A, B, C, D')
    )

    turn = models.CharField(
        verbose_name=_('Turn'), max_length=1,
        blank=True, null=True, db_index=True,
        help_text=_('Example: 1, 2')
    )

    # standings table info
    games_played = models.IntegerField(
        verbose_name=_("Games Played"), default=0)

    points = models.IntegerField(
        verbose_name=_("Points"), default=0)

    wins = models.IntegerField(
        verbose_name=_("Wins"), default=0)

    draws = models.IntegerField(
        verbose_name=_("Draws"), default=0)

    losses = models.IntegerField(
        verbose_name=_("Losses"), default=0)

    goals_for = models.IntegerField(
        verbose_name=_("Goals For"), default=0)

    goals_against = models.IntegerField(
        verbose_name=_("Goals Against"), default=0)

    goals_difference = models.IntegerField(
        verbose_name=_("Goals Difference"), default=0)
