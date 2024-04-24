# Номер автомобиля - r"[A-Z]\d{3}[A-Z]{2}\d{2,3}"
import re
text = input("Введите номер автомобиля в формате А123АА123: ")
number = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}')
if re.match(number,text):
    print("Номер указан верно")
else:
    print("Номер указан не верно")