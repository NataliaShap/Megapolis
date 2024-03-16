import csv

# функция высчитывает процент
def proc(stroka):
    return stroka * 100

with open('vacancy.csv', encoding='utf-8') as file, open('vacancy_procent.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file, delimiter=';')

    a=[] # a - список
    data[0].append('precent')
    for stroka in data[1:]:
        if stroka[0] != 'None':
            a.append(int(stroka[0]))
    sred=(sum(a) / len(a)) # sred - среднее значение

    for stroka in data[1:]:
        if stroka[0] != 'None':
            res.writerow(stroka)
        else:
            stroka = str(proc(sred))
            res.writerow(stroka)