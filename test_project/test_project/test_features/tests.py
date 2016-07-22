from django.test import TestCase

from feature_flipper.templatetags.feature_flipper import show_feature

from .models import Company


class FeatureFlipperTestCase(TestCase):
    """
    """
    fixtures = (
        'test_features/features',
    )

    def test_company_feature(self):
        """Test a company that can see a feature
        """
        self.assertTrue(
            show_feature(Company.objects.get(pk=1), 'restricted_feature'))

    def test_cannot_see(self):
        """A company without access to the feature can't see it.
        """
        self.assertFalse(
            show_feature(Company.objects.get(pk=3), 'restricted_feature'))

    def test_everyone(self):
        """A company can see a feature enabled for everyone.
        """
        self.assertTrue(
            show_feature(Company.objects.get(pk=3), 'feature_for_all'))

    def test_show_feature_everyone(self):
        """A company can see a feature they're attached to enabled for all.
        """
        self.assertTrue(
            show_feature(Company.objects.get(pk=2), 'feature_for_all'))
