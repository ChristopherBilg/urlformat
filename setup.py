import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urlformat",
    version="0.0.1",  # MAJOR.MINOR.MAINTENANCE
    author="Christopher Richard Bilger",
    author_email="christopherbigl@gmail.com",
    license="GNU General Public License v2 (GPLv2)",
    keywords="url format uri web address website search index",
    description="A package for formatting valid URL's.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristopherBilg/urlformat",
    packages=setuptools.find_packages(),
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
    python_requires=">=3"
)