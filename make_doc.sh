#!/bin/sh

cd docs
make clean
rm -f source/generated/*
python3 make_folioapi_rst.py
make html
cd ..

