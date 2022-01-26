..
    Copyright (C) 2022 Graz University of Technology.

    marc21converter is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

========================
 marc21converter
========================

.. image:: https://img.shields.io/github/license/tu-graz-library/marc21converter.svg
        :target: https://github.com/tu-graz-library/marc21converter/blob/master/LICENSE

.. image:: https://github.com/tu-graz-library/marc21converter/workflows/CI/badge.svg
        :target: https://github.com/tu-graz-library/marc21converter/actions

.. image:: https://img.shields.io/coveralls/tu-graz-library/marc21converter.svg
        :target: https://coveralls.io/r/tu-graz-library/marc21converter

.. image:: https://img.shields.io/pypi/v/marc21converter.svg
        :target: https://pypi.org/pypi/marc21converter

Marc21 datamodel

Further documentation is available on
https://marc21converter.readthedocs.io/


Development
===========

Install
-------

Choose a version of elasticsearch and a DB, then run:

.. code-block:: console
    
    pipenv run pip install -e .[all]
    pipenv run pip install invenio-search[elasticsearch7]
    pipenv run pip install invenio-db[postgresql,versioning]


Service
=========

** Create Marc21 Record**

Tests
=========

.. code-block:: console

    pipenv run ./run-tests.sh