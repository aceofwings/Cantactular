=============
Documentation
=============
Documenting processes and the code base are crucial to having others contribute. There are currently no strict
rules for documenting in Cantactular



***************
Setup
***************
Sphinx is used to generate the documentation. Install sphinx and once done at the root directory run

.. code-block:: bash

  make html

This will compile documentation to html and is placed within the *_build* directory

***************
Deployment
***************
Github pages is used to host the projects documentation. The gh-pages branch will have the compiled documentation placed
in the root directory. A subtree command is used to pick that folder and place its contents at the root of gh-pages.

Run this to add the html to the gh-pages

.. code-block:: bash

     git subtree push --prefix _build/html origin gh-pages
