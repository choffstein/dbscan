#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup

setup(name="dbscan",
	  version="1.0",
	  description="Density Based Spatial Clustering of Applications with Noise",
	  author = "Corey M. Hoffstein",
	  author_email="corey@newfoundresearch.com",
	  packages=['dbscan'],
	  package_dir={'dbscan': 'dbscan'})
