import os
"""
Resource locator is a helper for easily
"""
class ResourceLocator(object):

    ROOT_PATH  = None

    def __init__(self,root_path):
        super().__init__()
        self.ROOT_PATH = root_path

    def fetch_file(self,filename,relative_path=None):
        path = self.ROOT_PATH
        if relative_path is not None:
            path = os.join(path,relative_path)
        return os.join(path,filename)
