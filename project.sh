#!/bin/bash
if [ -z "$1" ]; then echo "var is unset" && exit 1; fi
mkdir $1
cd $1
mkdir bin $1 tests docs
touch $1/__init__.py
touch tests/__init__.py

cat > setup.py << EOF
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'dbax',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['$1'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
EOF

cat > tests/$1_tests.py <<EOF
from nose.tools import *
import $1

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
EOF
