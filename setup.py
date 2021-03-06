#!/usr/bin/env python2
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2017, c3V6a2Vy <c3V6a2Vy@protonmail.com>
# This software is under the terms of Apache License v2 or later.


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup # pylint: disable=F0401,E0611

setup(
    name='pyanova',
    author='c3V6a2Vy',
    author_email='c3V6a2Vy@protonmail.com',
    version='0.1.3',
    packages=['pyanova',],
    url='https://github.com/c3V6a2Vy/pyanova',
    license='Apache License 2.0',
    install_requires=[
        'pygatt',
        'pexpect'
    ],
    description='A Python Library for Anova Precision Cooker',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    )
)
