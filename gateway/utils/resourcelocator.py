import os
import logging
"""
Resource locator helps locates files and other resources.

cls.ROOT_PATH get set in the locator file
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
    @classmethod
    def get_locator(cls,relative_path=""):
        """
        get_locator - returns a resource locator within the project directory
        :param relative_path: specify a path relative to the projects ROOT_PATH
        """
        path = relative_path
        if cls.ROOT_PATH is None:
            raise NoPathSpecified("No ROOT_PATH specified")
        path = os.path.join(cls.ROOT_PATH,relative_path)
        if not os.path.isdir(path):
            raise NonExistentDirectory("Folder non existent ", path)
        locator = ResourceLocator(path)
        return locator

class NonExistentDirectory(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class NoPathSpecified(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
