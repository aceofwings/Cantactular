import json
from gateway.utils.resourcelocator import ResourceLocator

CONFIG_LOCATION = "config/canEngine/"

class Configuration(object):
    """
    Fetch engine configurations
    """
    engine_locator = None
    config_file = None
    json_dict = None
    environment = None

    def __init__(self,environment=None):
        super().__init__()
        self.engine_locator = ResourceLocator.get_locator(CONFIG_LOCATION)
        self.config_file = self.engine_locator.fetch_file("configuration.json","r")
        self.json_dict = json.load(self.config_file)
        if environment is None:
            self.environment = "development"
        else:
            if environment in self.json_dict["environments"]:
                self.environment = environment
            else:
                raise MisconfigurationExecption("No such environment" , environment)

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
                if term in config:
                    config = config[term]
                else:
                    return None
        return config

    @classmethod
    def conf_with_environment(cls, env):
        if env in self.json_dict["environments"]:
            return Configuration(env)
        else:
            return None

    def __environment(self,e=None):
            if e is not None:
                return self.json_dict["environments"][e]
            else:
                return self.json_dict["environments"][self.environment]

    @configProperty("can.interfaces")
    def interfaces():
        pass

    @configProperty("core.address")
    def core_socket_address():
        pass

    @configProperty("core.app_type")
    def core_type():
        pass

    @configProperty("server")
    def server_address():
        pass

    @configProperty("engine.max_ipc_connections")
    def max_ipc_connections():
        pass
    @configProperty("engine.limit_connections")
    def limit_connection():
        pass


class MisconfigurationExecption(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
