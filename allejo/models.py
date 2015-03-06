from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Championship(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200)

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
        verbose_name=_('Name'), max_length=100, db_index=True)

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

    def __unicode__(self):
        return self.name


class Match(models.Model):
    home = models.ForeignKey(
        'Player',
        verbose_name=_('Home player'),
        related_name='home_player_set',
        blank=True, null=True
    )

    home_score = models.IntegerField(
        verbose_name=_('Score home player'), blank=True, null=True
    )

    away = models.ForeignKey(
        'Player',
        verbose_name=_('Away player'),
        related_name='away_player_set',
        blank=True, null=True
    )

    away_score = models.IntegerField(
        verbose_name=_('Score away player'), blank=True, null=True
    )

    championship = models.ForeignKey(
        'Championship',
        verbose_name=_('Choice a championship'),
        blank=True, null=True
    )

    winner = models.ForeignKey(
        'Player',
        verbose_name=_('Player winner'),
        blank=True, null=True
    )

    game_date = models.DateTimeField(blank=True, null=True)

    category = models.CharField(
        verbose_name=_('Category'), max_length=100,
        blank=True, null=True, db_index=True)

    group = models.CharField(
        verbose_name=_('Group'), max_length=1,
        blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        return "%s %s - %s" % (self.championship.name, self.home, self.away)


class Standings(model.Model):
    championship = models.ForeignKey(
        'Championship',
        verbose_name=_('Choice a championship'),
        blank=True, null=True
    )

    player = models.ForeignKey(
        'Player',
        verbose_name=_('Player'),
        related_name='player_set',
        blank=True, null=True
    )

    category = models.CharField(
        verbose_name=_('Category'), max_length=100,
        blank=True, null=True, db_index=True)

    group = models.CharField(
        verbose_name=_('Group'), max_length=1,
        blank=True, null=True, db_index=True)

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
