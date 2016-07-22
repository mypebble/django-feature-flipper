from setuptools import find_packages, setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='django-feature-flipper',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
)
