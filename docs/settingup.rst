Setup Python Virtual Env
===========================
Crucial to not step on other package dependencies, it is recommended
to install the project under a virtual environment.


Install the virtual environment package via pip. Note there is an apt
package installer too but is not covered here.

.. code-block:: bash

  python3 -m pip install virtualenv
  # or
  pip3 install virtualenv

Run the following command in the project directory


.. code-block:: bash

  python3 -m virtualenv env


Activate the environment


.. code-block:: bash

  source env/bin/activate


Install the project

.. code-block:: bash

  python setup.py install

You should have the command *gateway* available to You

.. code-block:: bash

  gateway --version
