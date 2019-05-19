""" Test suite for the swydo library template.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the package is actually
being tested. If the package is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""

# Ugh: https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../src')

import pytest

def test_version():
    """ Test the library version.

    """
    from swydo import __version__
    assert __version__ == "1.2019.5.19"
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
