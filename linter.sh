#!/bin/bash

py_files=("urlformat/urlparser.py"
          "urlformat/urlbuilder.py"
          "urlformat/errors.py"
          "urlformat/robotparser.py"
          "urlformat/__init__.py"
          "tests/urltester.py"
          "tests/urlspeedtester.py"
          "setup.py")

for i in "${py_files[@]}"
do
    echo "Starting lint on ${i}"
    pylint ${i} --rcfile=setup.cfg
    pycodestyle ${i}
    flake8 ${i}
    yapf --style pep8 --diff ${i}
done

echo "Finished linting all files"
