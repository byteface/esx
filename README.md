<h1 align="center">
    <!-- <img src="https://image.freepik.com/free-vector/demonic-goat_71119-56.jpg"
    style="background-color:rgba(0,0,0,0);" height=230 alt="JavaScript: generate html with python 3!"> -->
    <br>
    JavaScript
    <br>
    <sup><sub><sup>JS API in python 3!</sup></sub></sup>
    <br>
</h1>

[![PyPI version](https://badge.fury.io/py/JavaScript.svg)](https://badge.fury.io/py/JavaScript.svg) 
[![Downloads](https://pepy.tech/badge/JavaScript)](https://pepy.tech/project/JavaScript)
[![Python version](https://img.shields.io/pypi/pyversions/JavaScript.svg?style=flat)](https://img.shields.io/pypi/pyversions/JavaScript.svg?style=flat)
[![Build status](https://travis-ci.com/byteface/JavaScript.svg?branch=master)](https://travis-ci.com/byteface/JavaScript.svg?branch=master)
[![Python package](https://github.com/byteface/JavaScript/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/byteface/JavaScript/actions/workflows/python-package.yml)


#### Contains

• [javascript](https://JavaScript.readthedocs.io/_modules/JavaScript/javascript.html) : js API in python 3 😳 <br />
• JSON : utils for loading / decorating / transforming<br />

See the docs/code for more features...
https://JavaScript.readthedocs.io/

or examples in the [repo...](https://github.com/byteface/JavaScript/tree/master/examples)


#### API


```python
from JavaScript import Math
print(Math.random())

from JavaScript import Array
myArr=Array(1,2,3)
print(myArr.splice(1))

from JavaScript import URL
url = URL('https://somesite.com/blog/article-one#some-hash')
print(url.protocol)
print(url.host)
print(url.pathname)
print(url.hash)

# you can use Global class to import all the js methods from the global namespace i.e
# from JavaScript.javascript import Global
# Global.decodeURIComponent(...
# Global.encodeComponent(...
# Global.setInterval(...

# from JavaScript.javascript import Date, String, Number
# etc..
```

You can use setInterval and clearInterval with params

```python

from JavaScript import setInterval, clearInterval

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

from JavaScript import setTimeout, clearTimeout

timeoutID = setTimeout(hi, 1000)

```

## DOCS

https://JavaScript.readthedocs.io/

### notes

Do some notes here


### CLI
There's a few args you can pass to JavaScript on the command line to help you out.

To launch the docs for a quick reference to the APIs use:

```python

python3 -m JavaScript -h

```

This command will attempt to generate a template from a webpage. (only simple pages for now)

```python

python3 -m JavaScript -d http://eventual.technology

```

Then you can edit/tweak it to get what you need and build new components quicker.


### EXAMPLE PROJECTS

There's several useage examples in the domonic repo so pull and have a look.


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
python -m unittest tests.test_javascript.TestCase.test_javascript_array
```

or to test a whole module
```bash
python -m unittest tests.test_javascript
```

to see coverage
```bash
coverage run -m unittest discover tests/
coverage report
```
