##check_prime_number.py

num=int(input('Type here: '))
i=2
for i in range(i,num):
    if (num%i==0):
        print(num,'not prime')
        break
else:
    print(num,"prime")
#stop
