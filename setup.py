#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "live_stylus",
    version = "0.1",
    author = "Allen.M",
    author_email = "menghonglun@gmail.com",
    description = "Convert stylus to css real time. Easily used by any web framwork.",
    licence = "MIT",
    keywords = "stylus css",
    url = "https://github.com/allenm/live-py-stylus",
    packages = ["live_stylus"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=["stylus","watchdog"]
)
