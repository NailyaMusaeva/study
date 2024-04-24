import math
x1 = float ( input ("введите координату А x1 = "))
y1 = float ( input ("введите координату А y1 = "))
x2 = float ( input ("введите координату В x2 = "))
y2 = float ( input ("введите координату В y2 = "))
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print ("AB = " + str(d))