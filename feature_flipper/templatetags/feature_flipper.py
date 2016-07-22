import string

from django import template

from ..models import get_feature_model


register = template.Library()


def show_feature(user, feature):
    """Return True/False whether the assigned feature can be displayed. This is
    primarily used in the template tag to determine whether to render the
    content inside itself.
    """
    FeatureFlipper = get_feature_model()
    return FeatureFlipper.objects.show_feature(user, feature)


@register.tag(name='flipper')
def do_flipper(parser, token):
    """The flipper tag takes two arguments: the user to look up and the feature
    to compare against.
    """
    nodelist = parser.parse(('endflipper',))
    tag_name, user_key, feature = token.split_contents()
    parser.delete_first_token()
    return FlipperNode(nodelist, user_key, feature)


class FlipperNode(template.Node):
    """Handles rendering the Feature Flipper guarded content.
    """
    def __init__(self, nodelist, user_key, feature):
        """Setup the tag
        """
        self.nodelist = nodelist
        self.user_key = user_key
        self.feature = feature

    def render(self, context):
        """Handle the actual rendering.
        """
        user = self._get_value(self.user_key, context)
        feature = self._get_value(self.feature, context)
        allowed = show_feature(user, feature)

        return self.nodelist.render(context) if allowed else ''

    def _get_value(self, key, context):
        """Works out whether key is a value or if it's a variable referencing a
        value in context and returns the correct value.
        """
        string_quotes = ('"', "'")

        if key[0] in string_quotes and key[-1] in string_quotes:
            return key[1:-1]
        if key in string.digits:
            return int(key)
        return context[key]
