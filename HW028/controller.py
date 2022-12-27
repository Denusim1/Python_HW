import ui
import all_com
from time import sleep


init_command = ui.start_message()
sleep(0.5)


while True:
    init_command = ui.chose_file_type()
    if init_command == '1':
        command = ui.chose_func()
        if command == '1':
            all_com.add_contact()
        if command == '2':
            all_com.find_contact()
        if command == '3':
            all_com.delete_contact()
        if command == '4':
            all_com.show_contact()
        if command == '5':
            exit()
            

    elif init_command == '2':
        sleep(0.5)
        command = ui.chose_func()
        if command == '1':
            all_com.add_contact_txt()
        if command == '2':
            all_com.find_contact_txt()
        if command == '3':
            all_com.delete_contact_txt()
        if command == '4':
            all_com.show_contact_txt()
        if command == '5':
            exit()
    elif init_command == '3':
        exit()
        
        
    else:
        print('Вы ошиблись с выбором команды. Попробуйте снова!')
        continue

