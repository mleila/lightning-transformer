#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='transformer',
    version='0.0.0',
    description='Describe Your Cool Project',
    author='Mohamed Leila',
    author_email='mohamed.leila.1989@gmail.com',
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url='https://github.com/mleila/lightning-transformer',
    install_requires=['pytorch-lightning'],
    packages=find_packages(),
)

