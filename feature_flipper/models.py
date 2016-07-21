from __future__ import unicode_literals

from django.db import models

from feature_flipper import flipper_settings


class FeatureFlipperQuerySet(models.query.QuerySet):
    """Provides a handler to look up feature flags for the given configuration.
    """
    def get_feature(self, feature):
        """Return the feature mapping.
        """
        return self.filter(feature=feature)

    def show_feature(self, user, feature):
        """Return True or False for the given feature.
        """
        user_filter = {
            self.model.USER_FEATURE_FIELD: user,
        }
        return self.get_feature(feature).filter(
            models.Q(**user_filter) | models.Q(everyone=True)).exists()


class AbstractFeatureFlipper(models.Model):
    """The basic feature flipper data that gets shared among all other
    applications
    """
    objects = FeatureFlipperQuerySet.as_manager()

    feature = models.CharField(
        max_length=15, choices=flipper_settings.FEATURE_FLIPPER_FLAGS)
    everyone = models.BooleanField(default=False)

    class Meta:
        abstract = True


class FeatureFlipper(AbstractFeatureFlipper):
    """A feature flipper hooked up to the Django User referenced by the user's
    settings. This provides a simple flipper class that most developers can use
    out of the box
    """
    USER_FEATURE_FIELD = 'user'

    user = models.ForeignKey(flipper_settings.AUTH_USER_MODEL)

    class Meta:
        swappable = 'FEATURE_FLIPPER_MODEL'
