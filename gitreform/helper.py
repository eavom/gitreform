import sys
import random

class AppHelper:
    pass

class FileHelper:
    def convert_file_to_list(me, file_source, file_path):
        pass

class DataHelper:
    @staticmethod
    def __get_list_of_messages():
        with open(f'{sys.path[0]}/collection/commit_messages.csv', 'r') as file:
            commit_messages = file.readlines()

        messages = [message.rstrip('\n') for message in commit_messages]
        return commit_messages

    def get_random_commit_message(self):
        commit_messages = self.__get_list_of_messages()

        message = commit_messages[random.randint(0, len(commit_messages)-1)].rstrip()

        return message
    
class WebHelper:
    pass

if __name__ == '__main__':
    datahelper = DataHelper()