# Ввести три целых числа, найти максимальное из них вар 1
print ( "Введите три числа: " )
a = int ( input("a = ") )
b = int ( input("b = ") )
c = int ( input("с = ") )
M1 = max(a,b,c)
print(M1)

# вар 2
print ( "Введите три числа: " )
a = int ( input("a = ") )
b = int ( input("b = ") )
c = int ( input("с = ") )
if b <= a >= c:
   print(a)
elif  a <= b >= c:
    print(b)   
elif a <= c >= b:
    print(c)

# вар 3
print ( "Введите три числа: " )
a = int ( input("a = ") )
b = int ( input("b = ") )
c = int ( input("с = ") )
if a > b and a > c:
   M = a
elif b > c:
   M = b
else:
    M = c
print (str(M))