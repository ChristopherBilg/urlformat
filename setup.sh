#!/bin/bash

echo "Removing build/ directory"
rm -rf build/

echo "Removing dist/ directory"
rm -rf dist/

echo "Removing urlformat.egg-info/ directory"
rm -rf urlformat.egg-info/

"Running setup.py command to generate previous directories"
python setup.py sdist bdist_wheel
