#!/bin/bash

disable_options="C0111,R0903,R0912"

echo "Starting lint on urlparser.py"
pylint urlparser.py --score=no --disable=$disable_options
pycodestyle urlparser.py
flake8 urlparser.py
yapf --style pep8 --parallel --diff urlparser.py

echo "Starting lint on urlbuilder.py"
pylint urlbuilder.py --score=no --disable=$disable_options
pycodestyle urlbuilder.py
flake8 urlbuilder.py
yapf --style pep8 --parallel --diff urlbuilder.py

echo "Starting lint on urltester.py"
pylint urltester.py --score=no --disable=$disable_options
pycodestyle urltester.py
flake8 urltester.py
yapf --style pep8 --parallel --diff urltester.py

echo "Starting lint on urlerrors.py"
pylint urlerrors.py --score=no --disable=$disable_options
pycodestyle urlerrors.py
flake8 urlerrors.py
yapf --style pep8 --parallel --diff urlerrors.py

echo "Starting lint on robotparser.py"
pylint robotparser.py --score=no --disable=$disable_options
pycodestyle robotparser.py
flake8 robotparser.py
yapf --style pep8 --parallel --diff robotparser.py

echo "Starting lint on urlspeedtester.py"
pylint urlspeedtester.py --score=no --disable=$disable_options
pycodestyle urlspeedtester.py
flake8 urlspeedtester.py
yapf --style pep8 --parallel --diff urlspeedtester.py

echo "Starting lint on ../setup.py"
pylint ../setup.py --score=no --disable=$disable_options
pycodestyle ../setup.py
flake8 ../setup.py
yapf --style pep8 --parallel --diff ../setup.py

echo "Finished linting all files"
