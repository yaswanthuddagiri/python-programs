lower = int(input("enter lower limit: "))
upper = int(input("Enter upper limit: "))
print("prime numbers between",lower,upper)
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
            else:
                print(num)
    
    
