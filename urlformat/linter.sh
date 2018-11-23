#!/bin/bash

echo "Starting lint on urlparser.py"
pylint urlparser.py --score=no --disable=C0111,R0912
pycodestyle urlparser.py
flake8 urlparser.py

echo "Starting lint on urlbuilder.py"
pylint urlbuilder.py --score=no --disable=C0111,R0912
pycodestyle urlbuilder.py
flake8 urlbuilder.py

echo "Starting lint on urltester.py"
pylint urltester.py --score=no --disable=C0111,R0912
pycodestyle urltester.py
flake8 urltester.py

echo "Starting lint on urlerrors.py"
pylint urlerrors.py --score=no --disable=C0111,R0912
pycodestyle urlerrors.py
flake8 urlerrors.py

echo "Starting lint on robotparser.py"
pylint robotparser.py --score=no --disable=C0111,R0912
pycodestyle robotparser.py
flake8 robotparser.py

echo "Starting lint on ../setup.py"
pylint ../setup.py --score=no --disable=C0111,R0912
pycodestyle ../setup.py
flake8 ../setup.py

echo "Finished linting all files"
