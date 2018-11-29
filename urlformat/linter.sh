#!/bin/bash

disable_options="C0111,R0903,R0912"
py_files=("urlparser.py"
          "urlbuilder.py"
          "urltester.py"
          "urlerrors.py"
          "robotparser.py"
          "urlspeedtester.py"
          "../setup.py")

for i in "${py_files[@]}"
do
    echo "Starting lint on ${i}"
    pylint ${i} --score=no --disable=$disable_options
    pycodestyle ${i}
    flake8 ${i}
    yapf --style pep8 --diff ${i}
done

echo "Finished linting all files"
