# python-soccerama
Wrapper over the data provided Soccerama API

## Installation

Install it yourself as:

    $ git clone git@github.com:tvl/python-soccerama.git

## Usage

The package has methods for gets some data from Soccerama.

```python
#/usr/bin/python
from soccerama import *

token = '__YOURTOKEN__'
init(token)

# Countries
print('Countries:')
for c in countries():
    print(c['iso_code'], c['name'])

# Competitions
print('Competitions:')
for c in competitions():
    print(c['name'])

# Seasons
print('Seasons:')
for s in seasons():
    print(s['name'])

# To view all bookmakers
print('Bookmakers:')
for b in bookmakers():
    print(b['name'])


```

