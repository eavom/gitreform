import sys
import random

class FileHelper:
    @staticmethod
    def convert_lines_to_list(content):
        content_list = [line.rstrip('\n') for line in content]
        return content_list
        

if __name__ == '__main__':
    pass