#!/usr/bin/env python
"""Setup script for hb-test"""
import sys
import os
from glob import glob
from setuptools import find_packages

__author__ = 'setten'


# changing Python version requirements.
if sys.version[0:3] < '3.6':
    sys.stderr.write("ERROR: hb-test requires Python Version 3.6 or above. Exiting.")
    sys.exit(1)


def file_doesnt_end_with(test, endings):
    """
    A little utility we'll need below, since glob() does NOT allow you to do exclusion on multiple endings!

    Return true if test is a file and its name does NOT end with any
    of the strings listed in endings.
    """
    if not os.path.isfile(test):
        return False
    for e in endings:
        if test.endswith(e):
            return False
    return True

# ---------------------------------------------------------------------------
# Basic project information
# ---------------------------------------------------------------------------


def find_package_data():
    """Find GWsol's package_data."""
    package_data = {}
    return package_data


def find_scripts():
    """Find GWsol scripts."""
    scripts = []
    #
    # All python files in abipy/scripts
    pyfiles = glob(os.path.join('hb-test', 'scripts', "*.py"))
    scripts.extend(pyfiles)
    return scripts


def cleanup():
    """Clean up the junk left around by the build process."""
    if "develop" not in sys.argv:
        import shutil
        try:
            shutil.rmtree('hb-test.egg-info')
        except:
            try:
                os.unlink('hb-test.egg-info')
            except:
                pass


# List of external packages we rely on.
# Note setup install will download them from Pypi if they are not available.
install_requires = []

# ---------------------------------------------------------------------------
# Find all the packages, package data, and data_files
# ---------------------------------------------------------------------------

# Get the set of packages to be included.
my_packages = find_packages(exclude=())

my_scripts = find_scripts()

my_package_data = find_package_data()

# Create a dict with the basic information
# This dict is eventually passed to setup after additional keys are added.
setup_args = dict(name="GWsol",
                  version="0.0.1",
                  description="Package for testing bandstructures.",
                  long_description="Package for testing bandstructures.",
                  author="Michiel van Setten",
                  author_email="mjvansetten@gmail.com",
                  # url=url,
                  # download_url=download_url,
                  license="license",
                  platforms="platforms",
                  keywords="keywords",
                  install_requires=install_requires,
                  packages=my_packages,
                  package_data=my_package_data,
                  scripts=my_scripts,
                  )


if __name__ == "__main__":
    from setuptools import setup
    setup(**setup_args)
    cleanup()
