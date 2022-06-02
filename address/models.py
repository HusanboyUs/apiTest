from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    """
    Stores predefined address of client, workshop or point of car pickup for repair.
    """
    country = models.CharField(verbose_name=_('country'), max_length=100,
                               help_text=_('country'))
    street = models.CharField(verbose_name=_('street'), max_length=100,
                              help_text=_('street'))
    city = models.CharField(verbose_name=_('city'), max_length=100,
                            help_text=_('city'))

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f"{self.city} {self.street}"

