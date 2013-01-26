#!/usr/bin/env python

# Work around a truly bizarre setuptools quirk. Oh, Python packaging.
try:
    import multiprocessing, logging
except ImportError:
    pass

from setuptools import setup

requirements = []

# Check for the presence of a Python 2.7-compliant unittest
try:
    import unittest
    unittest.TestCase.assertIs
    unittest.TestCase.assertIn
except (AttributeError, ImportError):
    requirements.append('unittest2 >= 0.5')

setup(
    name='chamomile',
    version='1.0.0',
    description='Jasmine-style assertions for unittest',
    url='https://github.com/enaeseth/chamomile',
    author='Eric Naeseth',
    author_email='eric@naeseth.com',
    license='MIT',
    packages=['chamomile'],
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
