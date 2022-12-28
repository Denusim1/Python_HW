import re
import message as mg


#1111111111
def show_contact():
    with open('HW029/base.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(mg.m_all)
        for row in lines:
            print(row)

#222222222222
def find_contact():
    name = input(mg.m_find)
    with open('HW029/base.txt', encoding="utf-8") as file:
        for line in file.readlines():
            if name in line:
                print (line)
                break
        else:
            print(mg.m_non)               

#33333333    
def find_position():
    position = input(mg.m_position)
    with open('HW029/base.txt', encoding="utf-8") as file:
        for line in file.readlines():
            if position in line:
                print (line)
                break
        else:
            print(mg.m_non) 
#4444444
def find_salary():
    print(mg.m_num_sol)
    num = input(mg.m_num_oper)
    if num == '1':
        little = 'z_1'
        with open('HW029/base.txt', encoding="utf-8") as file:
            for line in file.readlines():
                if little in line:
                    print (line)
                    break
            else:
                print(mg.m_non_z) 
    if num == '2':
        average = 'z_2'
        with open('HW029/base.txt', encoding="utf-8") as file:
            for line in file.readlines():
                if average in line:
                    print (line)
                    break
            else:
                print(mg.m_non_z) 
    if num == '3':
        high = 'z_3'
        with open('HW029/base.txt', encoding="utf-8") as file:
            for line in file.readlines():
                if high in line:
                    print (line)
                    break
            else:
                print(mg.m_non_z)
    if num == '4':
        exit() 
    
#5555555555
def add_contact():
    id = int(input(mg.m_id))
    first_name = input(mg.m_first_name)
    last_name = input(mg.m_last_name)
    position = input(mg.m_position)
    phone_number = input(mg.m_phone_number)
    salary = int(input(mg.m_salary))
    if salary < 30000:kf = 'z_1'
    if salary > 30000 and salary < 50000:kf = 'z_2'
    if salary > 50000:kf = 'z_3'
    new_contact = (id , first_name, last_name, position, phone_number, salary,kf)
    with open('HW029/base.txt', 'a') as file:
        file.write(', '.join(map(str, new_contact))+"\n")
        print(mg.m_append)

#6666666666
def delete_contact():
    name = input(mg.m_dell)
    with open('HW029/base.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
    pattern = re.compile(re.escape(name))
    with open('HW029/base.txt', "w", encoding="utf-8") as file:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
                print(mg.m_dell_cont)
                break
        
#777777
def update_contact():
    find_contact()
    print(mg.m_update)
    delete_contact()
    print(mg.m_new)
    add_contact()





# def add_contact():
#     id = input(mg.m_id)
#     first_name = input(mg.m_first_name)
#     last_name = input(mg.m_last_name)
#     position = input(mg.m_position)
#     phone_number = input(mg.m_phone_number)
#     salary = input(mg.m_salary)
#     with open('HW029/base.csv', 'a', newline = '',encoding="utf-8") as file:
#         fieldnames =  ['id', 'first_name', 'last_name', "position", "phone", "salary"]
#         writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({'id': id, 'first_name': first_name, 'last_name': last_name, 'position': position, "phone": phone_number, "salary": salary})
#         print(mg.m_append)


# def show_contact():
    
#     with open('HW029/base.csv', encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row['id'], row['first_name'], row['last_name'], row['position'], row['phone'], row['salary'])