from django.conf import settings

_DEFAULT_FEATURE_FLAGS = ()

FEATURE_FLIPPER_FLAGS = getattr(
    settings, 'FEATURE_FLIPPER_FLAGS',
    _DEFAULT_FEATURE_FLAGS)

AUTH_USER_MODEL = settings.AUTH_USER_MODEL

FEATURE_FLIPPER_MODEL = getattr(
    settings, 'FEATURE_FLIPPER_MODEL',
    'feature_flipper.FeatureFlipper')
