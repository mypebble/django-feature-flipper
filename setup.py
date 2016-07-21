from distutils.core import setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='django-feature-flipper',
    version='0.0.1',
    packages=[
        'feature_flipper',
    ],
    license='MIT',
    long_description=LONG_DESCRIPTION,
)
