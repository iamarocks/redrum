#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "redis==2.10.3",
    "wheel==0.23.0"
]

test_requirements = [
    "tox"
]

setup(
    name='redrum',
    version='0.1.0',
    description="A simple Redis ORM",
    long_description=readme + '\n\n' + history,
    author="Brent Hoover",
    author_email='brent@hoover.net',
    url='https://github.com/zenweasel/redrum',
    packages=[
        'redrum',
    ],
    package_dir={'redrum':
                 'redrum'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='redrum',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
