import sys
import random

class TextHelper:
    def __init__(self):
        pass

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