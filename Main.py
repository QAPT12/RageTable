from RageTable_Class import *

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
