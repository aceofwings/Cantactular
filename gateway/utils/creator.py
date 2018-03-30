from gateway.utils.resourcelocator import ResourceLocator
from gateway.templates import launcher

import shutil
import json
import os
import json


config_template = { 'environments' : {
        'production': {
            'can': {
                'interfaces': {
                    'can0' : "EVTCAN",
                    'can1' : "CANOPEN"
                }
            }
        },
        'development': {
            'can': {
                'interfaces': {
                    'vcan0' : "EVTCAN",
                    'vcan1' : "CANOPEN"
                }
            }
        },
        'shared' : {
            'core': {
                'address': "evt.gateway.core.sock",
                'app_type': "APPLICATION"
            },
            'server' : "../../gateway/temp/evt.gateway.core.sock",
            'engine':{
                'maxConnections' : 3
            },
            'interfaceTypes' : ["EVTCAN", "OPENCAN"]
        }
        }
 }

class ProjectComponent(object):
    pass

class Module(ProjectComponent):
    def __init__(self,name):
        self.name = name

    def create(self,path):
        folder_path = os.path.join(path,self.name)
        os.mkdir(folder_path)
        init_path = os.path.join(folder_path,'__init__.py')
        with open(init_path, 'w+') as f:
            pass

class Folder(ProjectComponent):
    def __init__(self,name,relative_path = None):
        self.name = name
        self.relative_path = relative_path

    def create(self,path):
        folder_path = path
        if self.relative_path is not None:
            folder_path = os.path.join(path,self.relative_path)
        folder_path = os.path.join(folder_path,self.name)
        os.mkdir(folder_path)



class ProjectCreator(object):
    components =[
    Module('controllers'),
    Folder('config'),
    Folder('temp'),
    Module('tests'),
    Module('commands'),
    Folder('canEngine',relative_path='config'),
    Folder('edsfiles',relative_path='config'),
    Folder('temp')
    ]

    def __init__(self,projectName, relative_path = None):
        if relative_path is not None:
            self.projectPath = ResourceLocator(os.path.join(relative_path, projectName))
        else:
            self.projectPath = ResourceLocator(os.path.join(os.getcwd(),projectName))
        self.projectName = projectName
        self.config = config_template

    def create_root_dirctory(self,**options):
        if not os.path.exists(self.projectPath.ROOT_PATH):
            os.mkdir(self.projectName)
        else:
            raise ProjectExists()

    def create_root_components(self,**options):
        for component in self.components:
            component.create(self.projectPath.ROOT_PATH)


    def create_and_build_config(self,**options):
        shutil.copy(launcher.__file__, self.projectPath.ROOT_PATH)

    def create_config(self,**option):
        file_path = os.path.join(self.projectPath.ROOT_PATH,"config/canEngine/configuration.json")
        with open(file_path, 'w+') as f:
            f.write(json.dumps(self.config,indent=4,sort_keys=True))

    def build_project(self,**options):
        self.create_root_dirctory(**options)
        self.create_root_components(**options)
        self.create_and_build_config(**options)
        self.create_config(**options)


class ProjectExists(Exception):
    pass
