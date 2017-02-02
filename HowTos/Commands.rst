=============
Commands, Testing and Execution
=============
   Once you have downloaded and installed the project, you now have access to the gateway's bin files. When

You can now execute::
     gateway [command]

There are several commands.
 * start -> starts the application
 * test -> Runs the test suite for gateway



--------------
Development
--------------
You might have noticed that if you want to change code, you have to build each
change. This is a hassle for frequent small changes. Run setup in development
mode.

run::
    python3 setup.py develop

This will create soft-link pointers to your project file
Now whenever you change your code, you should see it update automatically. 
