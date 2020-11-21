#-------------------------------------------------------------------------------
# Name:        Roark Creek
# Purpose:     To deliver secure stream encryption through use of a symmetrical key.
#
# Author:      Jordan Gloor
#
# Created:     25/08/2020
# Copyright:   (c) Jordan Gloor 2020
#-------------------------------------------------------------------------------

#Notes
	#A "sub-string not found" error typically means you used a character not included in the libraries.
import math
version_number = "0.2.1a"

def greeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek "+version_number+"           |\n|                                         |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit")
	#This sets a default key to save time when time
	processKey("111111111111111111111111")

def acceptKey():
	userKey=input("Enter 24-bit key: ")
	processKey(userKey)

def processKey(userKey):
	if len(userKey)!=24:
		print('Error! Bad key entered.')
	else:
		print("Hashing key and finding books...")
		keyBit=[]
		keyHashLib='mHUa_?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z'
		for x in userKey: keyBit.append(keyHashLib.index(x))
		keyHash_cryptBook=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3],99))
		keyHash_refBook=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3],99))
		keyHash_leafBook=int(math.fmod(keyBit[0]*keyBit[3],99))
		keyHash_seed1=int(math.fmod(keyBit[2]*keyBit[5],91))
		keyHash_seed2=int(math.fmod(keyBit[3]*keyBit[6],91))
		global leafBook
		leafBook=findNewBook(keyHash_leafBook,'leaf')
		global seed1
		seed1=findSeedValue(keyHash_seed1,'Z RbQc3fjBuPÑ~Gv{Y7sXLF%-|Ck)S(q&_<^JTMNi0:KEH6!p5.OI1VAa,W*+?>}$n8gñox@edDzwlrU2h=t`94y#m')
		global seed2
		seed2=findSeedValue(keyHash_seed2,'+|Gb6iñ!05jUdpJ%lVy3Oo`x(nIkE91~RTuDPLZYNQF84*-S=g#&2.Ht>_,WmÑf?esKrA7zMvh X$^Cwq@}Bc{a<):')
		print("Key accepted: "+str(userKey))

def findSeedValue(keyHash,library):
	i=0
	for x in library:
		if i==keyHash:
			global seed
			seed=x
			break
		else:
			i+=1
			continue
	return seed

def downstreamDecrypt():
	userCiphertext = str(input("Enter ciphertext to be decrypted: "))
	decryptedText=""
	i=0
	for x in range(len(userCiphertext)):
		if i==0:
			p1=seed1
			p2=seed2
		elif i==1:
			p1=userCiphertext[x-1]
			p2=seed1
		else:
			p1=userCiphertext[x-2]
			p2=userCiphertext[x-1]
		i+=1
		leafKey1=math.fmod(hashLeaf(p1)*hashLeaf(p2),99)
		leafKey2=math.fmod(hashLeaf(p1)+hashLeaf(p2),99)
		z=decryptLeaf(userCiphertext[x],leafKey1,leafKey2)
		decryptedText=str(decryptedText)+str(z)
	print("Decryption complete: "+decryptedText)

def downstreamEncrypt():
	userPlaintext = str(input("Enter plaintext to be encrypted: "))
	encryptedText=""
	i=0
	for x in range(len(userPlaintext)):
		if i==0:
			p1=seed1
			p2=seed2
		elif i==1:
			p1=encryptedText[x-1]
			p2=seed1
		else:
			p1=encryptedText[x-2]
			p2=encryptedText[x-1]
		i+=1
		leafKey1=math.fmod(hashLeaf(p1)*hashLeaf(p2),99)
		leafKey2=math.fmod(hashLeaf(p1)+hashLeaf(p2),99)
		z=encryptLeaf(userPlaintext[x],leafKey1,leafKey2)
		encryptedText=str(encryptedText)+str(z)
	print("Encryption complete: "+encryptedText)

def encryptLeaf(leaf,leafKey1,leafKey2):
	refBook=findNewBook(leafKey1,'ref')
	cryptBook=findNewBook(leafKey2,'crypt')
	refNum=refBook.index(leaf)
	output=cryptBook[refNum]
	return output

def decryptLeaf(leaf,leafKey1,leafKey2):
	RefBook=findNewBook(leafKey1,'ref')
	CryptBook=findNewBook(leafKey2,'crypt')
	cryptNum=CryptBook.index(leaf)
	output=RefBook[cryptNum]
	return output

def findNewBook(leafKey,library):
	openLib=open('libraries/'+library+'Lib1.txt','r')
	i=0
	for x in openLib:
		if i==leafKey:
			foundBook=str(openLib.readline())
			break
		else:
			i+=1
			continue
	openLib.close()
	return foundBook

def hashLeaf(leaf):
	hashProduct=leafBook.index(leaf)
	return hashProduct

def get_command():
	x = 0
	while x == 0:
		command = str(input("\nEnter command: "))
		if command == "k" or command == "key":
			return "key"
		elif command == "e" or command == "encrypt":
			return "encrypt"
		elif command == "d" or command == "decrypt":
			return "decrypt"
		elif command == "q" or command == "quit" or command == "exit":
			return "quit"
		else:
			print("\""+command+"\" bad input. Try again.")
			continue

def task(selected_task):
	if selected_task == "key":
		acceptKey()
	elif selected_task == "encrypt":
		downstreamEncrypt()
	elif selected_task == "decrypt":
		downstreamDecrypt()
	elif selected_task == "quit":
		global T
		T = 1

greeting()
T = 0
while T == 0:
	choice = get_command()
	task(choice)
