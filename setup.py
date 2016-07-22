from setuptools import find_packages, setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='django-feature-flipper',
    author='Pebble',
    author_email='scott.walton@mypebble.co.uk',
    description='A simple, customisable, feature flipper',
    url='https://github.com/mypebble/django-feature-flipper.git',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
)
