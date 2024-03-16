import csv

with open('vacancy.csv', encoding='utf-8') as file, open('vacancy_new1.csv', 'w', encoding='utf-8', newline='') as new_file:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file, delimiter=';')