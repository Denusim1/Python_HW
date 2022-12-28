import message as mg
import os
clear = lambda: os.system('clear')
clear()

def start_message():
    print(mg.m_start)
def chose_file_type():
    return input(mg.m_type)
