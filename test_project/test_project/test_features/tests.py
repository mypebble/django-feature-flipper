from django.template import Context, Template
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


class TemplateTagTestCase(TestCase):
    """Test the {% flipper %} template tag.
    """
    fixtures = (
        'test_features/features',
    )

    def render_restricted(self, company):
        """Run the actual flipper tag name with 'restricted_feature'
        """
        return self.render_template('''{% load feature_flipper %}
        {% flipper company 'restricted_feature' %}
        rendered
        {% endflipper %}''', company)

    def render_all(self, company):
        """Run the flipper tag with 'feature_for_all'
        """
        return self.render_template('''{% load feature_flipper %}
        {% flipper company 'feature_for_all' %}
        rendered
        {% endflipper %}''', company)

    def render_template(self, template, company):
        """Actually render the template
        """
        return Template(template).render(Context({'company': company}))

    def test_company_feature(self):
        """Template should render for the given company.
        """
        output = self.render_restricted(Company.objects.get(pk=1))
        self.assertIn('rendered', output)

    def test_cannot_see(self):
        """Template should not render for not accessible company.
        """
        output = self.render_restricted(Company.objects.get(pk=2))
        self.assertNotIn('rendered', output)

    def test_everyone(self):
        """A company can see a feature enabled for everyone.
        """
        output = self.render_all(Company.objects.get(pk=3))
        self.assertIn('rendered', output)

    def test_show_feature_everyone(self):
        """A company can see a feature they're attached to enabled for all.
        """
        output = self.render_all(Company.objects.get(pk=2))
        self.assertIn('rendered', output)
