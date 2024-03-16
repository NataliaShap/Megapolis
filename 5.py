import csv

with open('vacancy.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))
