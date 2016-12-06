# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.srt') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='money-monkey-py',
    version='1.0',
    description='Money Monkey Financial Manager',
    long_description=readme,
    author='Gergely Nyiri',
    author_email='gergely.nyiri@gmail.com',
    url='https://github.com/gnyiri/money-monkey-py',
    license=license,
    install_requires=required,
    packages=find_packages(exclude=('tests', 'docs'))
)
