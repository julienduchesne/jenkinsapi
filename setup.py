#!/usr/bin/env python
# coding=utf-8

import json
import os

from setuptools import setup, find_packages

package_root = os.path.dirname(os.path.realpath(__file__))
setup(
    name="jenkinsapi",
    version="0.5.1",
    description="JenkinsAPI fork",
    maintainer="Julien Duchesne",
    maintainer_email="jduchesne@coveo.com",
    url="",
    install_requires=[
        "pytz>=2014.4",
        "requests>=2.3.0",
        "six>=1.10.0"
    ],
    packages=find_packages()
)
