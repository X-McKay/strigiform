===============================
Strigiform
===============================


|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/strigiform.svg
   :target: https://pypi.org/project/strigiform/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/strigiform
   :target: https://pypi.org/project/strigiform
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/strigiform
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/strigiform/latest.svg?label=Read%20the%20Docs
   :target: https://strigiform.readthedocs.io/
   :alt: Read the documentation at https://strigiform.readthedocs.io/
.. |Tests| image:: https://github.com/X-McKay/strigiform/workflows/Tests/badge.svg
   :target: https://github.com/X-McKay/strigiform/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/X-McKay/strigiform/branch/develop/graph/badge.svg
   :target: https://codecov.io/gh/X-McKay/strigiform
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Strigiform is a monorepo of tools, applications, and services for Birders and Researchers.



Project Maturity and readiness
------------------------------

Strigiform is under active development and has not been tested
for use by others; many key workflows and best practices are still being worked
out and/or implemented. For information about the focus of future work,
please see TODOs & Roadmap.



Features
--------

* `Click`_ - Easy to use command line interface.
* `eBird API`_ - Get taxonomy, hotspots, and more from eBird
* `Streamlit`_ - Web app to visualize and interact with observation data
* `Vault`_ - Secret management
* `Terraform`_ - Infrastructure as code



Requirements
------------

`ASDF`_ for managing multiple runtime verisions.

`eBird API Key`_ to dyanamically use and access eBird data.

* Once an API Key has been obtained, store it in an Environment variable named **EBIRD_KEY**

Optional:
   * `AWS`_ - Instrastructure and storage
   * `Infracost`_ - Calculate cost of infrastructure prior to deployment


Installation
------------

You can install *strigiform* via pip_ from PyPI_:

.. code:: console

   $ pip install strigiform



TODOs & Roadmap
---------------

- CLI Reference
- Improve Unit Testing
- Reproducability testing
- Integration with Cloud Providers (AWS, GCP, Azure, etc.)
- Containerize Streamlit application
- Graph visualization of taxonomy and lifelist
- GeoHeatmap of observations


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
*strigiform* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits and inspiration
-----------------------


* `Cornell Lab of Ornithology`_

* This project was created using `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

* Approach to set-up inspired by `@twrodriguez`_'s `System Bootstrap`

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/X-McKay/strigiform/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://strigiform.readthedocs.io/en/latest/usage.html
.. _ASDF: http://asdf-vm.com/
.. _eBird API Key: https://ebird.org/data/download
.. _eBird API: https://documenter.getpostman.com/view/664302/S1ENwy59
.. _Streamlit: https://streamlit.io/
.. _Vault: https://www.vaultproject.io/
.. _Terraform: https://www.terraform.io/
.. _AWS: https://aws.amazon.com/
.. _Infracost: https://www.infracost.com/
.. _Click: https://click.palletsprojects.com/
.. _Cornell Lab of Ornithology: https://www.birds.cornell.edu/home/
.. _@twrodriguez: https://github.com/twrodriguez
.. _System Bootstrap: https://github.com/twrodriguez/system-bootstrap
