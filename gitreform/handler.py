import sys
import os
import random
import csv
import yaml
from pathlib import Path
from .options import SourceType, Level, ConfigType, App

class AppHandler:
    def __init__(self):
        try:
            config_handler = ConfigHandler(App.CONFIG_TYPE, App.CONFIG_NAME)
            self.app_config = config_handler.read_configurations()
            self.design_template = None
            self.github_username = None
            self.github_repository = None
        except:
            raise

class ConfigHandler:
    def __init__(self, config_type, config_path):
        current_path = os.path.dirname(__file__)
        
        self.config_type = config_type
        self.config_path = (os.path.abspath(os.path.join(current_path, os.pardir, config_path)))

    def read_configurations(self):
        config = None

        try:      
            if self.config_type == ConfigType.YAML:

                if App.VERBOSE: print(f'settings.yml : {self.config_path}')
                
                config = yaml.safe_load(Path(self.config_path).read_text())
            else:
                raise Exception('Unable to read settings.yml or it''s broken!')
        except(Exception):
            raise

        if config is None:
            raise Exception('Settings.yml is broken')
        else:
            return config

class FileHandler:
    
    def __init__(self, source_type, source_path):
        self.source_type = source_type
        self.source_path = source_path
        self.source_content = None

    def get_file_content(self):
        # sys.path[0]}/collection/commit_messages.csv'
        try:
            if self.source_type == SourceType.OFFLINE:
                with open(f'{sys.path[0]}/{self.source_path}', 'r') as file:
                    self.source_content = file.readlines()
            elif self.source_type == SourceType.ONLINE:
                self.source_content = csv.reader(self.source_path)
            else:
                raise Exception('Something went wrong while reading commit messages file!')
            
            if self.source_content is None:
                raise Exception('Source File is empty!')
        except Exception:
            raise


# class DataHandler:
#     def __init__(self):
#         pass

#     def get_random_commit_message(self):
#         commit_messages = self.__get_list_of_messages()

#         message = commit_messages[random.randint(0, len(commit_messages)-1)].rstrip()

#         return message
    
#     @staticmethod
#     def __get_list_of_messages():
        

#         messages = [message.rstrip('\n') for message in commit_messages]
#         return commit_messages

    
if __name__ == '__main__':
    # config_handler = ConfigHandler(ConfigType.YAML, 'settings.yml')
    # config_handler.set_configurations()

    # print(config_handler.config)
    pass