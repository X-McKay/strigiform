===============================
kingfisher
===============================


|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/kingfisher.svg
   :target: https://pypi.org/project/kingfisher/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/kingfisher
   :target: https://pypi.org/project/kingfisher
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/kingfisher
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/kingfisher/latest.svg?label=Read%20the%20Docs
   :target: https://kingfisher.readthedocs.io/
   :alt: Read the documentation at https://kingfisher.readthedocs.io/
.. |Tests| image:: https://github.com/X-McKay/kingfisher/workflows/Tests/badge.svg
   :target: https://github.com/X-McKay/kingfisher/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/X-McKay/kingfisher/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/X-McKay/kingfisher
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


kingfisher is a Python package that provides tools for Birders and Researchers to:

* Explore and visualize information for Birders
* Easily interact with eBird APIs.


Project Maturity and readiness
------------------------------

kingfisher is under active development; many key workflows and best practices are still being worked out.
More seamless interaction with eBird products is in development, as well as
general improvement the overall user experience.


A current major focus is visualization of user life-lists across various levels
of taxonomy and relevant categories.


Features
--------

* Retrieval of hotspots (eBird) via CLI and/or python
* Extracting the latest version of the eBird Taxonomy (species list for data entry and listing purposes across the world)



Requirements
------------

`ASDF`_ for managing multiple runtime verisions.

`eBird API Key`_ to dyanamically use and access eBird data.

* Once an API Key has been obtained, store it in an Environment variable named **EBIRD_KEY**


Installation
------------

You can install *kingfisher* via pip_ from PyPI_:

.. code:: console

   $ pip install kingfisher


Usage
-----

* IN PROGRESS

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*kingfisher* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

* Cornell University

* Cornell Lab of Ornithology

* This project was originally based on `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

* Credit to Tim Rodriguez for indirect influence of S&BP.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/X-McKay/kingfisher/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://kingfisher.readthedocs.io/en/latest/usage.html
.. _ASDF: http://asdf-vm.com/
.. _eBird API Key: https://ebird.org/data/download
