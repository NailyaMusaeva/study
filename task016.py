import csv 
a = input('Имя файла: ')
exmplfile = open(a+'.csv', 'w' ,encoding='UTF-16', newline='')
exmplwrtr = csv.writer(exmplfile, delimiter=';')
exmpldt = [['картошка'], ['морковь'], ['огурцы']]
for row in exmpldt:
    exmplwrtr.writerow(row)
exmplfile.close()
print('создан файл')
