# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 Graz University of Technology.
#
# marc21converter is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Marc21 datamodel"""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = []


extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    if name[0] == ":" or name in (""):
        continue
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=2.8",
    "pytest-runner>=3.0.0,<5",
]

install_requires = [
    "lxml>=4.6.2",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("marc21converter", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="marc21converter",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="Marc21 converter invenio",
    license="MIT",
    author="Philipp Gualdi",
    author_email="philipp.gualdi@tugraz.at",
    url="https://github.com/tu-graz-library/marc21converter",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "console_scripts": [
            "marc21converter = marc21converter.cli:cli",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 1 - Planning",
    ],
)
