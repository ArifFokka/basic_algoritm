#find_the_factorial

num = int(input("Enter a number: "))
factorial,i =1,1

for i in range (1,num+1):
    factorial=factorial*i
    #i+=1
print("The factorial of",num,"is",factorial)