import random


def list_from_text_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return [line for line in lines]


class RageTable:
    def __init__(self):
        self.table = list_from_text_file('RageSheet.txt')

    def roll_rage(self):
        result = self.table[random.randint(1, len(self.table)) - 1]
        print(result)


if __name__ == '__main__':
    rageTable = RageTable()
    while True:
        user_input = input('0 to quit, 1 to roll: ')
        match user_input:
            case '0':
                break
            case '1':
                rageTable.roll_rage()
            case _:
                print('wrong button idiot')
