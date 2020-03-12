#check_prime_number.py

n=int(input('Type here: '))
i,flag =1,1
for x in range(i, i<(n/2)):
       if (n % x) == 0:
           flag=0
           print(n,"is not a prime number")
           break
if flag == 0:
    print(n, "is not a prime number")
else:
    print(n, "is  a prime number")