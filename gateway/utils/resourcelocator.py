import os
"""
Resource locator helps locates files and other resources.

cls.ROOT_PATH get set in the locator file
"""
class ResourceLocator(object):

    ROOT_PATH  = None

    def __init__(self,root_path):
        super().__init__()
        self.ROOT_PATH = root_path

    @staticmethod
    def get_locator(cls,relative_path=None):
        """
        get_locator - returns a resource locator within the project directory
        :param relative_path: specify a path relative to the projects ROOT_PATH
        """
        path = relative_path
        locator = ResourceLocator(path)
        if cls.ROOT_PATH is None:
            if relative_path is None:
                raise NoPathSpecified("No ROOT_PATH or relative_path specified")
        else:
            path = os.join(cls.ROOT_PATH,relative_path)

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
