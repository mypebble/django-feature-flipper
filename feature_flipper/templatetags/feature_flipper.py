from django import template

from ..models import get_feature_model


register = template.Library()


def show_feature(item, feature):
    """Return True/False whether the assigned feature can be displayed. This is
    primarily used in the template tag to determine whether to render the
    content inside itself.
    """
    FeatureFlipper = get_feature_model()
    return FeatureFlipper.objects.show_feature(item, feature)


@register.tag(name='flipper')
def do_flipper(parser, token):
    nodelist = parser.parse(('endflipper',))
    tag_name, feature = token.split_contents()
    parser.delete_first_token()
    return FlipperNode(nodelist, feature)


class FlipperNode(template.Node):
    def __init__(self, nodelist, user, feature):
        self.nodelist = nodelist
        self.user = user
        self.feature = feature

    def render(self, context):
        allowed = show_feature(self.user, self.feature)
        if allowed:
            output = self.nodelist.render(context)
            return output
        else:
            return ''
