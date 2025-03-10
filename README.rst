.. _Optimus: https://optimus.readthedocs.io/
.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Node.js: https://nodejs.org
.. _Bootstrap frontend toolkit: https://getbootstrap.com/

===================
Sveetch Github home
===================

`My homepage on Github <https://sveetch.github.io>`_ to promote some things.

Developed with `Optimus`_ and `Bootstrap frontend toolkit`_.


Prerequisites
*************

* `Python`_>=3.8;
* `virtualenv`_;
* `pip`_;
* `Node.js`_>=18;
* GNU make (or any Makefile tool compatible);


Install
*******

Once prerequisites are filled, you just have to clone repository and run this
command line: ::

    make install


Usage
*****

Once installed you can build everything: ::

    make frontend mo html

This will build the development version in directory in ``dist/dev/``.

Finally you can then serve the static build: ::

    make server

Or push it anywhere on a web server since it is only a static site.

Going further
*************

See the Makefile help for details about available helpful tasks: ::

    make help

And see the `Optimus`_ documentation for more details on how to work on this project.

Deployment
**********

Deployment is done with `Github pages <https://docs.github.com/en/pages>`_ system.

Workflow
--------

* We are developing into master branch;
* Once a release is finalized, we bump version from ``cookiebaked.json``;
* Add a release into changelog file;
* Commit and push to master;
* Switch into branch ``github-pages``;
* Rebase the branch with master;
* Build into production mode;
* Push ``github-pages``;
* The GitHub Actions workflow will this branch update and will deploy site;
