from setuptools import find_packages, setup

try:
    with open('README.rst') as f:
        LONG_DESCRIPTION = f.read()
except:
    LONG_DESCRIPTION = ''

setup(
    name='django-feature-flipper',
    author='Pebble',
    author_email='scott.walton@mypebble.co.uk',
    description='A simple, customisable, feature flipper',
    url='https://github.com/mypebble/django-feature-flipper.git',
    version='0.0.4',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
)
