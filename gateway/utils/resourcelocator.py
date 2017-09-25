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
        path = cls.ROOT_PATH
        locator = ResourceLocator(path)
        if relative_path is not None:
            path = os.join(cls.ROOT_PATH,relative_path)
        locator.ROOT_PATH = path
        return locator
