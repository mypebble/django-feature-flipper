from os import path
from setuptools import find_packages, setup

README_PATH = path.join(path.dirname(path.abspath(__file__)), 'README.md')

try:
    import m2r
    LONG_DESCRIPTION = m2r.parse_from_file(README_PATH)
except (ImportError, IOError, FileNotFoundError):
    # m2r not installed or file does not exist
    LONG_DESCRIPTION = ''

setup(
    name='django-feature-flipper',
    author='Pebble',
    author_email='scott.walton@mypebble.co.uk',
    description='A simple, customisable, feature flipper',
    url='https://github.com/mypebble/django-feature-flipper.git',
    version='0.1.3',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'django',
    ]
)
