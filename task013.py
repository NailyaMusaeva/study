print ("Введите имя, отчество и фамилию: " )
s = input ()
listFIO=s.split(' ')
s=listFIO[0][:1]+'. '+listFIO[1][:1]+'. '+listFIO[2]
print (s)