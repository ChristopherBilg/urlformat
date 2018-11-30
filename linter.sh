#!/bin/bash

disable_options="C0111,R0903,R0912"
py_files=("urlformat/urlparser.py"
          "urlformat/urlbuilder.py"
          "urlformat/urltester.py"
          "urlformat/errors.py"
          "urlformat/robotparser.py"
          "urlformat/sitemapparser.py"
          "urlformat/urlspeedtester.py"
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
