# -*- coding: utf-8 -*-

import lshashpy3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(this_directory, 'CHANGES.rst'), encoding='utf-8') as f:
    changes = f.read()

required = ['numpy', 'bitarray']

setup(
    name='lshashpy3',
    version=lshashpy3.__version__,
    packages=['lshashpy3'],
    author='Kay Zhu',
    author_email='me@kayzhu.com',
    maintainer='Loreto Parisi',
    maintainer_email='loretoparisi@gmail.com',
    url="https://github.com/loretoparisi/lshash",
    description='A fast Python 3 implementation of locality sensitive hashing with persistance support.',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    license='MIT License',
    requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        ]
)