#!/bin/sh

python3 setup.py clean
debian/rules clean
echo "Remove build MANIFEST dist *.egg-info *.pyc *.pyo __pycache__"
rm -rf build/ MANIFEST dist/ *.egg-info
find . -name '*.pyc' -delete
find . -name '*.pyo' -delete
find . -name '__pycache__' -delete
#cd docs
#make clean
#echo "Remove generated docs"
#rm -f source/generated/*
#cd ..
