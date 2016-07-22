from django.contrib import admin
from django.db.models import ManyToManyField

from .models import get_feature_model


FeatureFlipper = get_feature_model()


def _is_m2m(user_field):
    field = FeatureFlipper._meta.get_field(user_field)
    return isinstance(field, ManyToManyField)


def get_horizontal_filter():
    """If the USER_FEATURE_FIELD is a M2M field, set it to filter_horizontal.
    """
    user_field = FeatureFlipper.USER_FEATURE_FIELD
    return (user_field, ) if _is_m2m(user_field) else ()


def get_flat_filter():
    """If USER_FEATURE_FIELD is _not_ M2M, just return the regular fields.
    """
    user_field = FeatureFlipper.USER_FEATURE_FIELD

    return ('feature', user_field) if not _is_m2m(user_field) else ('feature',)


class FeatureFlipperAdmin(admin.ModelAdmin):
    """Manage the Feature Flipper
    """
    filter_horizontal = get_horizontal_filter()

    list_display = 'feature', 'everyone'
    list_filter = get_flat_filter()
    list_editable = 'everyone',

    search_fields = 'feature',


admin.site.register(FeatureFlipper, FeatureFlipperAdmin)
