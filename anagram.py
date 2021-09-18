def Anagram(d1): 
      
    # empty dictionary for anagrams together 
    dict = {} 
  
    # traversal 
    for val in d1: 
          
        # sorts list
        key = ''.join(sorted(val)) 
          
        if key in dict.keys(): 
            dict[key].append(val) 
        else: 
            dict[key] = [] 
            dict[key].append(val) 
  
    # traverse dictionary and join keys together 
    result = "" 
    for key,value in dict.items(): 
        result = result + ' '.join(value) + ' '
  
    return result 
  
d1=['vks','sai', 'kiran', 'nairk','ias','god','dog','skv','yaswanth','htnawsay']
print("Words: ",d1)
print("Anagram: ",Anagram(d1))
