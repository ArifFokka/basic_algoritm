#the largest among three different numbers
a=int(input('Type Num:'))
b=int(input('Type Num:'))
c=int(input('Type Num:'))

if a>b:
    if a>c:
        print(a,"Is the largest Number.")
    else:
        print(c,"Is the largest Number.")
else:
    if b>c:
        print(b,'Is the largest Number.')
    else:
        print(c,"Is the largest Number.")


