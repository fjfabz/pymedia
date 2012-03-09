#!/usr/bin/env python
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'media.core',
    version = '0.0.1dev',
    author = 'David Andreoletti',
    packages = find_packages(),
    description = 'Media Core'
)

print "packages==>";print find_packages()
