#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name="pydbus-manager",
	version=None,
	description="DBus.ObjectManager implementation for pydbus",
	author="Sébastien Corne",
	author_email="sebastien@seebz.net",
	url="https://github.com/Seebz/pydbus-manager",
	license="WTFPL",

	packages=["pydbus_manager"],
	install_requires=["pydbus>=0.6"]
)
