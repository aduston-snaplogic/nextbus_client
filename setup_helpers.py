"""
setup_helpers.py - Define some custom commands and helper methods for setup.py

Author: Adam Duston
License: BSD-3-Clause
"""

from distutils.cmd import Command
from distutils.log import INFO
from os import path, getcwd
import subprocess
import re


class PylintCommand(Command):
    """
    Custom command for running PyLint with setuptools.
    """

    # Set a default value for options
    description = 'run Pylint on all files in the project'
    user_options = [
        # The format is (long option, short option, description).
        ('rcfile=', None, 'path to Pylint config file'),
        ('pylint-bin=', None, 'Path to the Pylint binary')
    ]
    rcfile = None
    pylint_bin = None

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.rcfile = None
        self.pylint_bin = None

    def finalize_options(self):
        """Post-process options."""
        if self.rcfile:
            assert path.exists(self.rcfile), (
                'Pylint config file {0} does not exist.'.format(self.rcfile)
            )

        if self.pylint_bin:
            assert path.exists(self.pylint_bin), (
                'Pylint binary {0} does not exist.'.format(self.pylint_bin)
            )
        else:
            self.pylint_bin = which('pylint')
            assert self.pylint_bin is not None, (
                'No pylint binary found in $PATH'
            )

    def run(self):
        """Run the command with subprocess."""
        if self.pylint_bin:
            command = [self.pylint_bin]
        else:
            command = [which('pylint')]

        if self.rcfile:
            command.append('--rcfile=%s' % self.rcfile)

        command.append(getcwd() + '/nextbus_client')
        self.announce(
            'Running linting command: {0}'.format(' '.join(command)),
            level=INFO)
        # Call the command. Don't use any sort of check_call or exit code checks.
        # Just want to see the pylint output when this is run.
        subprocess.call(command)


class BehaveCommand(Command):
    """
    Custom command for running behave with setuptools.
    """

    # Set a default value for options
    description = 'run behave on all files in the project'
    user_options = [
        # The format is (long option, short option, description).
        ('rcfile=', None, 'path to behave config file'),
        ('features', None, 'path to the features you want to run'),
        ('behave-bin=', None, 'Path to the behave binary')
    ]
    rcfile = None
    behave_bin = None
    features = None

    def initialize_options(self):
        """Set default values for options."""
        pass

    def finalize_options(self):
        """Post-process options."""
        if self.rcfile:
            assert path.exists(self.rcfile), (
                'behave config file {0} does not exist.'.format(self.rcfile)
            )

        if self.features:
            assert path.exists(self.features), (
                'Specified features {0} cannot be found'.format(self.features)
            )
        else:
            self.features = "{0}/{1}".format(getcwd(), 'features')

        if self.behave_bin:
            assert path.exists(self.behave_bin), (
                'behave binary {0} does not exist.'.format(self.behave_bin)
            )
        else:
            self.behave_bin = which('behave')
            assert self.behave_bin is not None, (
                'No behave binary found in $PATH'
            )

    def run(self):
        """Run the command with subprocess."""
        if self.behave_bin:
            command = [self.behave_bin]
        else:
            command = [which('behave')]

        if self.rcfile:
            command.append('--rcfile=%s' % self.rcfile)

        command.append(self.features)
        self.announce(
            'Running linting command: {0}'.format(' '.join(command)),
            level=INFO)
        # Call the command. Use check_call to ensure an error is thrown if tests fail.
        subprocess.check_call(command)


def which(command):
    """
    Use which to determine the path to the given binary

    :arg command: Name of the command binary to search for
    :return: String containing the path to the command binary, or None if it isn't found in the PATH.
    """
    process = subprocess.run(['which', command], stdout=subprocess.PIPE)
    if process.returncode == 0:
        return process.stdout.decode('utf-8').strip('\n')
    return None


def get_version(module):
    """
    Parse the version number from the module directory's __init__.py file

    :param module: Directory for the module to return a version for.
    :return: Version number as a string.
    """
    regex = re.compile(r"__version__\s+=\s+'(\d+\.\d+\.\d+)'")
    # Use a version.py if one exists. Otherwise use __init__.py
    read_file = '{0}/version.py'.format(module)
    if not path.exists(read_file):
        read_file = '{0}/__init__.py'.format(module)
    with open(read_file, 'r') as version_file:
        match = regex.search(version_file.read())
        if match:
            return match.group(1)
        return None
