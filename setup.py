#!/usr/bin/env python

import io
from setuptools import setup

with io.open('README') as description_file:
  long_description = description_file.read()

setup(
    name = "live_stylus",
    version = "0.2.4",
    author = "Allen.M",
    author_email = "menghonglun@gmail.com",
    description = "Convert stylus to css real time. Easily used by any web framwork.",
    license = "MIT",
    keywords = "stylus css",
    url = "https://github.com/allenm/live-py-stylus",
    packages = ["live_stylus"],
    long_description= long_description ,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=["stylus","watchdog"]
)
