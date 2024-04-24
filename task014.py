# Номер автомобиля - r"[A-Z]\d{3}[A-Z]{2}\d{2,3}RUS"
import re
text = input("Введите номер автомобиля: ")
number = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}RUS')
if re.match(number,text):
    print("Номер указан верно")
else:
    print("Номер указан не верно")