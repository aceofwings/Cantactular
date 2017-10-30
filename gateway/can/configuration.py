import json
from gateway.utils.resourcelocator import ResourceLocator

CONFIG_LOCATION = "config/canEngine/"

class Configuration(object):
    """
    Fetch engine configurations
    """
    engine_locator = ResourceLocator.get_locator(CONFIG_LOCATION)
    config_file = None
    json_dict = None
    environment = None

    def __init__(self,environment=None):
        super().__init__()
        self.config_file = self.engine_locator.fetch_file("configuration.json","r")
        self.json_dict = json.load(self.config_file)
        if environment is None:
            self.environment = "development"

    def configProperty(p=None):
        def _configProperty(function):
            def wrapper(*args,**kwargs):
                configInstance = args[0]
                terms = p.split('.')
                return configInstance.__fetch_term(terms)
            return wrapper
        return _configProperty

    def __fetch_term(self,terms):
        config = self.__environment()
        for term in terms:
            try:
                config = config[term]
            except KeyError:
                config = self.__environment("shared")
                config = config[term]
        return config

    def __environment(self,e=None):
            if e is not None:
                return self.json_dict["environments"][e]
            else:
                return self.json_dict["environments"][self.environment]

    @configProperty("can.interfaces")
    def interfaces(self):
        pass

    @configProperty("core.address")
    def core_socket_address():
        pass

    @configProperty("engine.maxConnections")
    def maximum_number_connections():
        pass
