from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from feature_flipper.models import AbstractFeatureFlipper


class Company(models.Model):
    """
    """
    company_name = models.CharField(max_length=10, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        """
        """
        return self.company_name


class TestFeatureFlipper(AbstractFeatureFlipper):
    """
    """
    USER_FEATURE_FIELD = 'company'

    company = models.ForeignKey(Company)
