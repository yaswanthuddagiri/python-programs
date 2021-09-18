# initializing string
test_str = 'sai is good . He has Classes now. Classes help understand better . '

# printing original string
print("The original string is : " + str(test_str))

# initializing replace mapping
repl_dict = {'yash' : 'ranker', 'Classes' : 'They' }

# Replace duplicate Occurrence in String
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
	if ele in repl_dict:
		if ele in res:
			test_list[idx] = repl_dict[ele]
		else:
			res.add(ele)
res = ' '.join(test_list)

# printing result
print("The string after replacing : " + str(res))
