import csv

# Функция, чтобы найти название компании
def search(company, data):
    for stroka in data:
        if stroka[-1] == company:
            return stroka
    return None

with open('vacancy.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))

    company = input()
    while company != 'None':
        res = search(company, data)
        if res == None:
            print('К сожалению, ничего не удалось найти')
        else:
            print(f'В {res[-1]} найдена вакансия: {res[-2]}. З/п составит: {res[0]}')
        company = input()