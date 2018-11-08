#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    'python-pcre>=0.7',
    'unidecode>=0.4.19',
    'nltk>=3.1',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pampo',
    version='0.1.0',
    description="Package to extract named entities from texts written in Portuguese",
    long_description=readme,
    author="Arian Pasquali",
    author_email='arrp@inesctec.pt',
    url='https://github.com/LIAAD/py-pampo',
    packages=[
        'pampo',
    ],
    package_dir={'pampo':
                 'pampo'},
    entry_points={
        'console_scripts': [
            'pampo=pampo.pampo:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='pampo',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
