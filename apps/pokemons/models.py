from django.db import models
from django.utils.translation import gettext_lazy as _


class Pokemon(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)

    height = models.IntegerField(_('Height'))
    weight = models.IntegerField(_('Weight'))

    order = models.IntegerField(_('Order'))

    class Meta:
        db_table = 'pokemons'
        verbose_name = _('Pokemon')
        verbose_name_plural = _('Pokemons')

    def __str__(self):
        return self.name
