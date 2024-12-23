
from enum import Enum

class ConfigType(Enum):
    YAML = 'YAML'
    JSON = 'JSON'
    XML = 'XML'
    INI = 'INI'

class Level(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class SourceType(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'

class GitHubURL(Enum):
    BASE_URL = 'https://github.com/'
    CONTRIBUTION_URI = 'contributions/'
    USERS_URI = 'users/'

class App:
    CONFIG_TYPE = ConfigType.YAML
    CONFIG_NAME = 'settings.yml'
    VERBOSE = True
    TITLE = '''
                _
     _______   (_) __    _____
    / __  / / / / / /   / /_\ \ 
   / /_/ / / /_/ /-/_  / /__/ /
   \__, /_/ /_/  \__/ /_/ \_\ 
   /____/
    '''