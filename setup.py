from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='drf_url_prefix_viewset',

    version='1.0.0',
    description='Helpful mixins for logical nesting of Django Rest Framework ViewSets',
    long_description='',

    url='http://github.com/weargoggles/drf-url-prefix-viewset',

    author='Pete Wildsmith',
    author_email='pete@weargoggles.co.uk',

    license='BSD',

    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',

    'License :: OSI Approved :: BSD 2-clause',

    'Programming Language :: Python :: 2',
    ],

    packages=['drf_url_prefix_viewset'],

    install_requires=[
        'djangorestframework>2,<3',
    ],
)
