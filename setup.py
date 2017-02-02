import os
import sys
from setuptools import setup, find_packages


setup(name='evtgateway',
      version='0.1',
      description='Gateway for RIT REV1 Sport Bike',
      url='https://github.com/aceofwings/Evt-Gateway',
      author='EVT RIT',
      author_email='EVT@RIT.EDU',
      packages=find_packages(),
      scripts= ['bin/gateway'],
      license='MIT',
      include_package_data=False,
      package_data={ '': ['*.txt', '*.rst']},
      zip_safe=False)


BIN_PATH = '/usr/local/bin'
