# Python program to left rotate array

# Function to rotate arrays in Python
def rotateArrayLeft(arr, R, n):
    for i in range(R):
    	firstVal = arr[0]
    	for i in range(n-1):
    		arr[i] = arr[i+1]
    	arr[n-1] = firstVal

# Taking array input from user
arr = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter number of elements of the array: "))
arr = []
print("Enter elements of the array :")
for i in range(n):
  numbers = int(input())
  arr.append(numbers)
R = int(input("Enter rotation count: "))

# Printing array 
print("Initial Array :", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
	
# Calling function for left Rotating array 
rotateArrayLeft(arr, R, n)

# Printing new array 
print("\nArray after rotation: ", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
