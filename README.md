itch-roulette
==========

[![Build Status](https://travis-ci.org/icbat/itch-roulette.svg?branch=master)](https://travis-ci.org/icbat/itch-roulette)

A roulette-type system for itch.io


To test locally:

1. `virtualenv venv`
2. `pip install -r requirements.txt`
3. `python server.py`
4. Go to localhost:5000

## Python versions

Right now, this is only compatible with python 2.x thanks to the use of urllib2. To make this usable with Python 3.x, the first step will be to replace these dependencies by using the [2to3](https://docs.python.org/2/glossary.html#term-to3) tool 