<h1 align="center">
    esx
    <br>
    <sup><sub><sup>JS API in python 3!</sup></sub></sup>
    <br>
</h1>

[![PyPI version](https://badge.fury.io/py/esx.svg)](https://badge.fury.io/py/esx.svg) 
[![Downloads](https://pepy.tech/badge/esx)](https://pepy.tech/project/esx)
[![Python version](https://img.shields.io/pypi/pyversions/esx.svg?style=flat)](https://img.shields.io/pypi/pyversions/esx.svg?style=flat)
[![Build status](https://travis-ci.com/byteface/esx.svg?branch=master)](https://travis-ci.com/byteface/esx.svg?branch=master)
[![Python package](https://github.com/byteface/esx/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/byteface/esx/actions/workflows/python-package.yml)


#### Contains

• js API in python 3


#### API


```python
from esx.javascript import Math
print(Math.random())

from esx.javascript import Array
myArr=Array(1,2,3)
print(myArr.splice(1))

from esx.javascript import URL
url = URL('https://somesite.com/blog/article-one#some-hash')
print(url.protocol)
print(url.host)
print(url.pathname)
print(url.hash)

# you can use Global class to import all the js methods from the global namespace i.e
# from esx.javascript.esx import Global
# Global.decodeURIComponent(...
# Global.encodeComponent(...
# Global.setInterval(...

# from esx.javascript.esx import Date, String, Number
# etc..
```

You can use setInterval and clearInterval with params

```python

from esx.javascript import setInterval, clearInterval

x=0

def hi(inc):
    global x
    x = x+inc
    print(x)

test = setInterval(hi, 1000, 2)
import time
time.sleep(5)
clearInterval(test)
print(f"Final value of x:{x}")

```

Or for a single delayed function call use setTimeout, clearTimeout

```python

from esx.javascript import setTimeout, clearTimeout

timeoutID = setTimeout(hi, 1000)

```

## DOCS

https://esx.readthedocs.io/

### notes

currently forking over from domonic.

### Join-In
Feel free to contribute if you find it useful.

Email me, message me directly if you like or create a discussion on here.

If there are any methods you want that are missing or not complete yet or you think you can help make it better just update the code and send a pull request.

I'll merge and releaese asap.


### run tests

There are tests used during dev. They are useful as code examples and to see what still needs doing.

See Makefile to run all tests:

```bash
make test
```

or to test a single function:
```bash
python -m unittest tests.test_esx.TestCase.test_esx_array
```

or to test a whole module
```bash
python -m unittest tests.test_esx
```

to see coverage
```bash
coverage run -m unittest discover tests/
coverage report
```
