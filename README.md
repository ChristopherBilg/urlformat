# urlformat
URL formatter for web addresses written in Python

This URL parsing/building class can handle any and all correctly formed URL's. Feel free to use any of the code and if you have any improvements please feel free to fork this repo. and push updates to me. Thank you.

It should be noted that I try to maintain a high level of PEP codestyle and linting guidelines. I used the PIP package manager with the pylint, pycodestyle and flake8 packages.

Installation:
```console
python3 pip -m install urlformat
```
or
```console
pip install urlformat
```

Usage:
```python
import urlformat

x = urlformat.UrlParser("https://www.google.com")
x = x.get_scheme()

print(x)

Output: https
```
