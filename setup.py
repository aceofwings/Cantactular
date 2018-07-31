import os
import sys
from pathlib import Path




try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup , find_packages


INSTALL_PATH = '/etc/gateway'
TEMP_PATH = '/etc/gateway/temp'
ENGINE_CONF_PATH = os.path.join(INSTALL_PATH,'config/canEngine')
EDS_FILES_CONF_PATH = os.path.join(INSTALL_PATH, 'config/edsfiles')

try:
    path = Path(os.path.join(INSTALL_PATH,EDS_FILES_CONF_PATH))
    path.mkdir(parents=True)
except:
    print("/config/temp exists in server file")


setup(name='evtgateway',
      version='0.4.3',
      description='Gateway for RIT REV1 Sport Bike',
      url='https://bitbucket.org/evt/gateway-applications',
      data_files = [(ENGINE_CONF_PATH, ['gateway/config/canEngine/configuration.json']),
      (INSTALL_PATH,['gateway/templates/launcher.py']),
      (TEMP_PATH,[])],
      author='EVT RIT',
      author_email='EVT@RIT.EDU',
      packages=find_packages(),
      scripts= ['bin/cansetup'],
      install_requires=['evtcantools'],
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

#ONLY SHOULD RUN on Raspian Production environment...
os.system("cp bin/gateway.service /etc/systemd/system/gateway.service")
os.system("chmod +x bin/gateway.start")
os.system("systemctl enable gateway.service")
