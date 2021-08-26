list1 = []
num = int(input("Enter size of list "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
    
 
print("Second highest number is : ",\
      sorted(list1)[-4])
