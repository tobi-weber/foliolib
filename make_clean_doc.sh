#!/bin/sh

cd docs
make clean
echo "Remove generated docs"
rm -f source/generated/*
#rm -f source/files/*
cd ..
