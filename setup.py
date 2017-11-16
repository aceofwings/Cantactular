import os
import sys
from setuptools import setup, find_packages


setup(name='evtgateway',
      version='0.3',
      description='Gateway for RIT REV1 Sport Bike',
      url='https://bitbucket.org/evt/gateway-applications',
      author='EVT RIT',
      author_email='EVT@RIT.EDU',
      packages=find_packages(),
      scripts= ['bin/cansetup'],
      license='MIT',
      include_package_data=False,
      package_data={ '': ['*.txt', '*.rst']},
      zip_safe=False,
      entry_points ={
      'console_scripts': [
                  'gateway = gateway.exec:main_func_gateway',
              ],
      })
BIN_PATH = '/usr/local/bin'
