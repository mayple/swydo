"""
Setup script for the swydo library.
"""
from os import path
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))
__version__ = None

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.readlines()

_config = {
    "name": "swydo",
    "author": "Alon Diamant",
    "author_email": "alon@mayple.com",
    "description": "Swydo Python SDK (swydo)",
    "url": "https://www.github.com/mayple/swydo",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "package_dir": {"": "src"},
    "packages": find_packages("src"),
    "install_requires": requires,
    "setup_requires": requires,
    "include_package_data": True,
    "classifiers": {
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    },
}


def main():
    """ Execute the setup commands.

    """

    def version():
        """ Get the local package version. """
        namespace = {}
        path = Path("src", _config["name"], "__version__.py")
        exec(path.read_text(), namespace)
        return namespace["__version__"]

    _config.update({
        "version": version(),
    })
    setup(**_config)
    return 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
