import os
import logging
"""
Resource locator helps locates files and other resources within project
cls.ROOT_PATH get set in the locator file.
"""
logger = logging.getLogger(__name__)

class ResourceLocator(object):

    def __init__(self,root_path):
        super().__init__()
        self.ROOT_PATH = root_path

    def fetch_file_path(self,filename):
        path = os.path.join(self.ROOT_PATH,filename)
        return os.path.abspath(path)

    def fetch_file(self,filename,mode):
        file_resource = open(self.fetch_file_path(filename),mode)
        return file_resource
    @classmethod
    def get_locator(cls,relative_path="",lazy=False):
        """
        get_locator - returns a resource locator within the project directory
        :param relative_path: specify a path relative to the projects ROOT_PATH
        can also be an absolute path.
        """
        path = relative_path
        if cls.ROOT_PATH is None:
            raise NoPathSpecified("No ROOT_PATH specified")
        path = os.path.join(cls.ROOT_PATH,relative_path)
        if not os.path.isdir(path) and  not lazy:
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
