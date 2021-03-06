#!/usr/bin/env python

from setuptools import setup

setup(
    name='virtualenvwrapper.gem',
    version='0.2',
    description='Plugin for virtualenvwrapper to automatically '
                'encapsulate inside the virtual environment'
                'any gems installed when the venv is activated',
    author='Rach Belaid',
    author_email='dev@ironbraces.com',
    url='https://github.com/rach/virtualenvwrapper.gem',
    namespace_packages=['virtualenvwrapper'],
    packages=['virtualenvwrapper'],
    install_requires=[
        'virtualenv',
        'virtualenvwrapper>=2.11',
    ],
    entry_points={
        'virtualenvwrapper.post_activate_source': [
            'gem = virtualenvwrapper.gem:post_activate_source',
            ],
        'virtualenvwrapper.pre_deactivate_source': [
            'gem = virtualenvwrapper.gem:pre_deactivate_source',
        ],
    }
)
