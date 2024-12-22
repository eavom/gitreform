from enum import Enum

class Level(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class SourceType(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'

class ConfigType(Enum):
    YAML = 'YAML'
    JSON = 'JSON'
    XML = 'XML'
    INI = 'INI'

class App:
    CONFIG_TYPE = ConfigType.YAML
    CONFIG_NAME = 'settings.yml'
    VERBOSE = True