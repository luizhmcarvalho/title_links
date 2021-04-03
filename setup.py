# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

version = '0.0.1'
requirements = parse_requirements("requirements.txt")

setup(
	name='title_links',
	version=version,
	description='Links using DocType title instead of name as Description',
	author='MaxMorais',
	author_email='max.morais.dmm@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir) for ir in requirements]
)
