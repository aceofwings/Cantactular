#!/usr/bin/python3
"""
exec.py

Helps find local project launcher. Changes current working directory until
launcher is found.

This allows us to call gateway locally anywhere in our project.  Changing
working directories to a known point in the project will allow for the an easier
way to map project assets.

If it successfully finds the launcher file, our working directory should now
be at the top level of this project, gateway-applications.

"""
import os
import sys
from gateway.command import gatewayCommandLine

def main_func_gateway():
    gatewayCommandLine()
    
