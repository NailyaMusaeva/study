#Ввести с клавиатуры в одну строку имя, отчество и фамилию, разделив их пробелом. Вывести имя.
print ("Введите имя, отчество и фамилию: " )
s = input ()
n=s.find (" ")
print (n)
s1 = s[:n]
print (s1)

#Ввести с клавиатуры в одну строку имя, отчество и фамилию, разделив их пробелом. Вывести имя, отчество, фамилию с новых строк
print ( "Введите имя, отчество и фамилию:" )
s = input()
n = s.find ( " " )
name = s[:n]   	# вырезать имя
s = s[n+1:]
n = s.find ( " " )
name2 = s[:n]   	# вырезать отчество 
s = s[n+1:]      	# осталась фамилия 
print ( str(name), str(name2), str(s), sep="\n")
