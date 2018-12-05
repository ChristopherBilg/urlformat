"""
Module for use by PyPI to install the "urlformat" package.
"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# setuptools for PyPI integration
setuptools.setup(
    name="urlformat",
    version="0.1.0",  # MAJOR.MINOR.MAINTENANCE
    author="Christopher Richard Bilger",
    author_email="christopherbigl@gmail.com",
    license="GNU General Public License v2 (GPLv2)",
    keywords="url format uri web address website search index",
    description="A package for formatting valid URL's.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristopherBilg/urlformat",
    packages=["urlformat"],  # packages are directories of modules (*.py files)
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.3")
