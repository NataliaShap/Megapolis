import csv

with open('vacancy.csv', encoding='utf-8') as file, open('vacancy_hash.csv', 'w', encoding='utf-8') as new_h:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_h, delimiter=';')

    res.writerow(data[0])
    new = {}
    for stroka in data[1:]:
        new = {stroka[-1]:[stroka[0], stroka[1], stroka[2], stroka[3]]}
    res.writerow(new)