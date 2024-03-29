#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from setuptools import setup, find_packages
import os

# Extract central version information
with open(os.path.join(os.path.dirname(__file__), "VERSION")) as version_file:
    version = version_file.read().strip()


setup(
    name="DigLab2Tools",
    version=version,
    packages=find_packages(),

    author="Julia Sprenger, Jeremy Garcia",
    description="diglab2ando is a tool that allows automatically creating a directory where data and metadata from a "
                "neuroscientific experiment are stored, and that follows the AnDO (Animal Data Organization) "
                "specifications ( https://int-nit.github.io/AnDO/ ), using as input a filled pdf form or a redcap "
                "survey/form generated using the DigLaB tool used at INT",
    license='MIT',
    install_requires=[],
    include_package_data=True,
    python_requires='>=3.7',
    extras_require={
        'test': ['pytest']
    }
)
