#!/bin/bash

echo "Removing build/ directory"
rm -rf build/

echo "Removing dist/ directory"
rm -rf dist/

echo "Removing urlformat.egg-info/ directory"
rm -rf urlformat.egg-info/

echo "Running setup.py command to generate previous directories"
python3 setup.py sdist bdist_wheel

echo "Uploading the dist/ directory (distribution) to the Test PyPI server"
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

echo "Installing the newly uploading package from the Test PyPI server"
python3 -m pip install --index-url https://test.pypi.org/simple/ urlformat

echo "Uploading the dist/ directory (distribution) to the official PyPI server"
twine upload dist/*
