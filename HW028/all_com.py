import csv
import re
import message as mg



def add_contact():
    name = input(mg.m_name)
    phone = input(mg.m_phone)
    new_contact = [name, phone]
    with open('HW028/phonebook.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(new_contact)
        print(mg.m_append)

def find_contact():
    name = input(mg.m_find)
    with open('HW028/phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if name == row[0]:
                print(*row)
                break
            else:
                print(mg.m_non)
                break

def delete_contact():
    name = input(mg.m_dell)
    temp_list = []
    with open('HW028/phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            temp_list.append(row)
        for item in temp_list:
            if name in item:
                temp_list.remove(item)
                print(mg.m_dell_cont)
                break              
        with open('HW028/phonebook.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(temp_list) 

def show_contact():
    with open('HW028/phonebook.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        print(mg.m_all)
        for row in reader:
            print('{:<10} {:<10}'.format(*row))


def add_contact_txt():
    name = input(mg.m_name)
    phone = input(mg.m_phone)
    new_contact = (name , phone)
    with open('HW028/phonebook.txt', 'a') as file:
        file.write(', '.join(map(str, new_contact))+"\n")
        print(mg.m_append)

def find_contact_txt():
    name = input(mg.m_find)
    with open('HW028/phonebook.txt', encoding="utf-8") as file:
        for line in file.readlines():
            if name in line:
                print (line)
                break
        else:
            print(mg.m_non)               
    

def delete_contact_txt():
    name = input(mg.m_dell)
    with open('HW028/phonebook.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
    pattern = re.compile(re.escape(name))
    with open('HW028/phonebook.txt', "w", encoding="utf-8") as file:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
                print(mg.m_dell_cont)
        
            
def show_contact_txt():
    with open('HW028/phonebook.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(mg.m_all)
        for row in lines:
            print(row)










