from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

_BN = {
    'blank': True,
    'null': True
}


class Champioship(models.Model):

    name = models.CharField(
        verbose_name=_(u'Name'),
        max_length=100,
    )

    max_players = models.PositiveIntegerField(
        verbose_name=_(u'Max of players')
    )

    started_at = models.DateTimeField()

    players = models.ManyToManyField(
        'Player',
        verbose_name=_(u'Players')
    )

    class Meta:
        verbose_name = _('Champioship')
        verbose_name_plural = _('Champioships')

    def __unicode__(self):
        pass


class Player(models.Model):

    name = models.CharField(
        verbose_name=_(u'Name'),
        max_length=100,
    )

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

    def __unicode__(self):
        pass


class Match(MPTTModel):

    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')

    home = models.ForeignKey(
        'Player',
        verbose_name=_(u'Home player'),
        related_name='home_player_set',
        **_BN
    )

    home_score = models.IntegerField(
        verbose_name=_(u'Score home player'),
        **_BN
    )

    away = models.ForeignKey(
        'Player',
        verbose_name=_(u'Away player'),
        related_name='away_player_set',
        **_BN
    )

    away_score = models.IntegerField(
        verbose_name=_(u'Score away player'),
        **_BN
    )

    champioship = models.ForeignKey(
        'Champioship',
        verbose_name=_(u'Choice a champioship'),
        **_BN
    )

    winner = models.ForeignKey(
        'Player',
        verbose_name=_(u'Player winner'),
        **_BN
    )

    game_date = models.DateTimeField(
        **_BN
    )

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        pass
