from django.contrib import admin

from .models import get_feature_model


FeatureFlipper = get_feature_model()


@admin.register(FeatureFlipper)
class FeatureFlipperAdmin(admin.ModelAdmin):
    """Manage the Feature Flipper
    """
    filter_horizontal = FeatureFlipper.USER_FEATURE_FIELD,

    list_display = 'feature', 'everyone'
    list_filter = 'feature',
    list_editable = 'everyone',

    search_fields = 'feature',
