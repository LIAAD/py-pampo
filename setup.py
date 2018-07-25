#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

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
    long_description=readme + '\n\n' + history,
    author="Arian Pasquali",
    author_email='arrp@inesctec.pt',
    url='https://bitbucket.org/liaad/pypampo',
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
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='pampo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
