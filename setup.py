"""
setup.py - Setup script for the nextbus_client module

Author: Adam Duston
License: BSD-3-Clause
"""
from setuptools import setup
from setup_helpers import PylintCommand, BehaveCommand, get_version, parse_requirements

VERSION = get_version('nextbus_client') or '0.0.0'

setup(
    name='nextbus_client',
    version=VERSION,
    author="Adam Duston",
    author_email="compybara@protonmail.com",
    url="https://github.com/compybara/nextbus_client",
    license="BSD-3-Clause",
    packages=['nextbus_client'],
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    tests_require=parse_requirements('requirements-test.txt'),
    cmdclass={
        "test": BehaveCommand,
        "lint": PylintCommand
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
