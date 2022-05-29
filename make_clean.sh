#!/bin/sh

python3 setup.py clean
debian/rules clean
rm -rf build/ MANIFEST dist/ *.egg-info
find . -name '*.pyc' -delete
find . -name '*.pyo' -delete
find . -name '__pycache__' -delete
