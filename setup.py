# -*- coding: utf-8 -*-
"""Setup.py to import local modules."""

from setuptools import find_packages, setup

setup(
    name="Full-Stack-BDD-Automation-Framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "behave",
        "playwright",
        "pytest-playwright",
        "pytest",
        "python-dotenv",        
    ],
    description="Full stack BDD Automation Framework",
)
