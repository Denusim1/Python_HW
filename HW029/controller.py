import ui2
import all_com
from time import sleep
from export import export_csv, export_json

init_command = ui2.start_message()
sleep(0.5)

while True:
    init_command = ui2.chose_file_type()
    if init_command == '1':
        all_com.show_contact()
    if init_command == '2':
        all_com.find_contact()
    if init_command == '3':
        all_com.find_position()
    if init_command == '4':
        all_com.find_salary()
    if init_command == '5':
        all_com.add_contact()
    if init_command == '6':
        all_com.delete_contact()
    if init_command == '7':
        all_com.update_contact()
    if init_command == '8':
        export_json()
    if init_command == '9':
        export_csv()
    if init_command == '10':
        exit()    
    






