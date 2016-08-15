# Feature Flipper

A set of simple feature flipper template tags that can be easily extended.

## Installation

To install this, simply `pip install django-feature-flipper`.

## Usage

Configure your `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = (
  ...
  'feature_flipper',
  ...
)
```

This gives you access to the basic feature flipping models and template tags.
You can then use the basic `FeatureFlipper` that turns flags on and off
depending on your user, or customise your own.

### Basic Feature Flipper

Set the flag choices in your `settings.py` file as:

```python
FEATURE_FLIPPER_FLAGS = (
  ('simple_feature', u'Simple Feature'),
  ('beta_testing', u'Beta Testing'),
)
```

When you add features, simply add flags here and your application will be able
to access the new flags immediately.

### Custom Feature Flipper

To customise the feature flipper you can just extend
`feature_flipper.models.AbstractFeatureFlipper` with your own field. This
provides a major advantage over the basic flipper by letting you determine your
own reference for filtering out whether users get a feature or not.

First, extend the `AbstractFeatureFlipper` model:

```python
from feature_flipper.models import AbstractFeatureFlipper


class MyFeatureFlipper(AbstractFeatureFlipper):
  """
  """
  USER_FEATURE_FIELD = 'company'

  company = models.ForeignKey('myapp.Company')
```

The `USER_FEATURE_FIELD` sets the field that should be used for lookups when
determining whether to show the feature to a user. The final part is to
reference this in your `settings.py`:

```python
FEATURE_FLIPPER_MODEL = 'myapp.MyFeatureFlipper',
```

## Using in Templates

To use the feature flipper in your templates, just load the `feature_flipper`
library and use the `flipper` template tag:

```html
{% load feature_flipper %}

<ul class="features">
  {% flipper request.user "simple_feature" %}
  <li><a href="/simple">Simple feature</a></li>
  {% endflipper %}

  {% flipper request.user "beta_testing" %}
  <li><a href="/testing">Beta-testing feature</a></li>
  {% endflipper %}
</ul>
```

### The `feature` tag

The `feature` template tag is a simple template tag that takes two arguments:

1. The user requesting access
2. The feature string to check for

For custom feature flippers, the `user` argument is simply the alternative user
identifier, for example the user's organisation.

## Supported Django Versions

This supports Django 1.9 and later.

| Feature Flipper | Django |
|-----------------|--------|
|      0.0.7      |   1.9  |
