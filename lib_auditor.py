#Library Auditor
#Checks libraries for duplicate books

import os

def list_duplicates(seq):
	seen = set()
	seen_add = seen.add
	#adds all elements it doesn't know yet to seen and all other to seen_twice
	seen_twice = set( x for x in seq if x in seen or seen_add(x) )
	#turn the set into a list
	return list( seen_twice )

Z=1
while Z==1:
	lib=str(input("Enter a library file name (no extension): "))
	if bool(os.path.exists('libraries/'+lib+'.txt')) is False:
		print("Library \""+lib+".txt\" does not exist! Try again.")
	else:
		library=open('libraries/'+lib+'.txt','r',encoding='utf8')
		a = []
		for x in library: a.append(x)
		print(list_duplicates(a))
		library.close()
		continue
