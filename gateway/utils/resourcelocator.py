import os
import logging
"""
Resource locator is a helper for easily
"""
logger = logging.getLogger(__name__)

class ResourceLocator(object):

    def __init__(self,root_path,mode='r'):
        super().__init__()
        self.ROOT_PATH = root_path
        self.mode = mode

    def fetch_file_path(self,filename,relative_path=None):
        path = self.ROOT_PATH
        if relative_path is not None:
            path = os.path.join(path,relative_path)
        return os.path.join(path,filename)

    def fetch_file(self,filename,relative_path=None):
        file_resource = open(self.fetch_file_path(filename,relative_path=relative_path),self.mode)
