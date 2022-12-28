import pandas as pd
import json
import codecs

def export_csv():
    df = pd.read_csv('HW029/base.txt', sep=',')
    df.to_csv('HW029/output.csv')

def export_json():
    wordfile = 'HW029/base.txt'
    file = open(wordfile, encoding="utf8")
    textline = file.readlines()
    id = []
    first_name = []
    last_name = []
    position = []
    phone_number = []
    salary = []
    z = []
    dictionary = []
    for x in range(len(textline)):
        if textline[x].strip():
            dataline = textline[x]
            splited = dataline.split(",")
            id.append(splited[0])
            first_name.append(splited[1].split(","))
            last_name.append(splited[2].split(","))
            position.append(splited[3].split(","))
            phone_number.append(splited[4].split(","))
            salary.append(splited[5].split(","))
            z.append(splited[6].strip("\n ' '"))

            
            dictionary = [{'id': id, 'first_name': first_name, 'last_name': last_name, 
            'position': position, 'phone_number': phone_number, 'salary': salary, 'z': z}
            for id, last_name, first_name, position, phone_number,salary, z in zip(id, last_name, first_name, position, phone_number,salary, z)]

    with codecs.open('HW029/output.json', 'w', encoding='utf8') as output:
        json.dump(dictionary, output, ensure_ascii=False)
    
