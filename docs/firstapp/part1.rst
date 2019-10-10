======================
Your First App Part 1
======================

In this tutorial you will learn how to setup, configure and write an application to print out Battery Voltages. At this point
you should have created a python virtual environment and have installed the project.


***************
Requirements
***************
You should have **can-utils** installed so virtual or hard interfaces can be established. This is crucial to send and receive test messages.

An operating system which supports can-utils or can like interfacing. In this case Ubuntu 19.04 is being used but has been tested in 16.04.



*****************
Starting a project
*****************

Go to a desired location and run

.. code-block:: bash

   gateway app batteryvoltages


This will generate a *batteryvoltages* directory

The directory will contain the following structure

-/batteryvoltages - project dirrectory

-----/commands - custom commands to run your application

-----/config - configuration files

-----/controllers - where your controllers containing your methods to handle certain message

-----/tests - where testing for certain parts of the app are located

-----/launcher.py  --- responsible for preloading and locating files to load your application files
