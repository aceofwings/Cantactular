==========
Testing
==========
Testing our code is very important for several reasons. Code as it increases in
volume, increases in the number of dependencies. By having a foundation of
test cases we can  catch errors in code and make sure refactoring/changes does
not disturb program flow.

-----------
Foundation
-----------
We can begin by simply testing code at the module level. Each module and its
methods should be fully covered but not to the extent of how it would be
implemented in application.

**Main Modules**

Main modules contain one file "*tests.py*" This file is responsible for testing the dependencies
between submodules and loading submodule tests. If there are no submodules, then its function acts as a
basic unitest case.

**Sub Modules**

Submodules are structured  below the initial module directory and usually have the form:
::

    import Gateway.can.message

where Gateway.can is the main module and message is a submodule. In this case each submodule, will have
a test.py which will contain the unitest case structure but will be loaded from the can module
"tests.py".

tests.py
------------------

tests.py is responsible for running sub module tests and any main module code. This file should also cover behavior of the module as a whole.

**loading submodules**

In tests.py if there are any submodule tests that need loading override:
::

    load_tests(loader, tests, pattern) returns TestSuite()

Note it must be Testsuite or a subclass of TestSuite

==============
Running Tests
==============
execute:
::

    gateway tests
