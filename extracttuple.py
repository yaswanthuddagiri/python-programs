# Extract digits from Tuple list
from itertools import chain

# initializing list
test_list = [(12, 34), (3, 91), (4, 10), (8, 2)]

# printing original list
print("The original list is : " + str(test_list))

# Extract digits from Tuple list
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
	for ele in sub:
		res.add(ele)

# printing result
print("The extracted digits : " + str(res))

