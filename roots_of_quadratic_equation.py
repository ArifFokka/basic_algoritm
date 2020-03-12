#quadratic equation ax2+bx+c=0.

from math import sqrt
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
D=b**2 - 4*a*c

if D>=0:
    x1=(((-b)+sqrt(D)) /(2*a))
    x2 = (((-b) - sqrt(D)) / (2 * a))
    print(x1, 'and', x2, 'as root')
else:
    rp=b/(2*a)
    ip=sqrt(-D)/(2*a)
    print(rp+ip,'and', (rp-ip),'as root')