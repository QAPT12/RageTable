import random


def list_from_text_file(file_name):
        '''
        Returns: list where each item is a line from the RageSheet text file
        '''
        with open(file_name) as f:
            lines = f.readlines()
            return [line for line in lines]

class RageTable:

    def __init__(self):
        self.table = list_from_text_file('RageSheet.txt')

    def roll_rage(self):
        result = self.table[random.randint(1, len(self.table)) - 1]
        print(result)
        