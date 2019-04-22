# Swydo Python SDK (swydo)

[![PyPI version](https://badge.fury.io/py/swydo.svg)](https://badge.fury.io/py/swydo)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/swydo.svg)](https://pypi.python.org/pypi/swydo/)
[![Build Status](https://travis-ci.com/mayple/swydo.svg?branch=master)](https://travis-ci.com/mayple/swydo)

> A Python 3 module to interact with the Swydo API.

Developed in [Mayple](https://www.mayple.com).

## Install

```sh
pip install swydo
```

## Example

```python
import logging
import math
import random

import swydo

logging.basicConfig()
```

## Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](https://github.com/mayple/swydo/issues/new).

Install with:
```sh
$ virtualenv .venv -p python3
$ . .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```
and run the tests with:
```sh
(.venv) $ pip install -r tests/requirements.txt
(.venv) $ pytest tests/
```
documentation can be generated like this:
```sh
(.venv) $ pip install -r doc/requirements.txt
(.venv) $ sphinx-build -b html doc doc/_build/html
```

## Related Projects

Used [cookiecutter Python library template](https://github.com/mdklatt/cookiecutter-python-lib) by [mdklatt](https://github.com/mdklatt).

## Author

**Alon Diamant (advance512)**

* [github/advance512](https://github.com/advance512)
* [Homepage](http://www.alondiamant.com)
