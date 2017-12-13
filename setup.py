# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='articleinfo',
    version='0.1.0',
    description='Get article information from your entered citation text.',
    long_description=readme,
    author='Yuto Mizutani',
    author_email='yuto.mizutani.dev@gmail.com',
    install_requires=[],
    url='https://github.com/YutoMizutani/articleinfo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

