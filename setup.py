# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gemafo',
    version='0.1.0',
    description='Gematik Afo Model',
    long_description=readme,
    author='Stephan Waldtmann',
    author_email='stephan@waldtmann.de',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
