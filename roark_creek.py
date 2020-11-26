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
version_number = "0.2.2a"

def greeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek "+version_number+"           |\n|                                         |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit")
	#This sets a default key to save time when testing
	processKey("111111111111111111111111")

def acceptKey():
	userKey=input("Enter 24-bit key: ")
	processKey(userKey)

def processKey(userKey):
	if len(userKey)!=24:
		print("Error! Key must be exactly 24 characters long.")
	else:
		print("Hashing key and finding books...")
		keyBit=[]
		keyHashLib='mHUa_?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z'
		for x in userKey: keyBit.append(keyHashLib.index(x))
		global keyHash_cryptMult
		keyHash_cryptMult=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5]+keyBit[6]*keyBit[7]+keyBit[8]*keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]*keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]*keyBit[21]+keyBit[22]*keyBit[23],1011))
		global keyHash_refMult
		keyHash_refMult=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],1011))
		keyHash_leafBook=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1011))
		keyHash_seed1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11],91))
		keyHash_seed2=int(math.fmod(keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],91))
		keyHash_seedBook1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1011))
		keyHash_seedBook2=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23],1011))
		global leafBook
		leafBook=findNewBook(keyHash_leafBook,'leaf')
		seedBook1=findNewBook(keyHash_seedBook1,'seed')
		seedBook2=findNewBook(keyHash_seedBook2,'seed')
		global seed1
		seed1=findSeedValue(keyHash_seed1,seedBook1)
		global seed2
		seed2=findSeedValue(keyHash_seed2,seedBook2)
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

def downstream(userInput,action):
	outputText=""
	if action=='decrypt':staticText=userInput
	i=0
	for x in range(len(userInput)):
		if i==0:
			p1=seed1
			p2=seed2
		elif i==1:
			p1=staticText[x-1]
			p2=seed1
		else:
			p1=staticText[x-2]
			p2=staticText[x-1]
		i+=1
		refKey=math.fmod(hashLeaf(p1)*hashLeaf(p2)*keyHash_refMult,1010)
		cryptKey=math.fmod(hashLeaf(p1)+hashLeaf(p2)*keyHash_cryptMult,1010)
		if action=='encrypt': z=encryptLeaf(userInput[x],refKey,cryptKey)
		if action=='decrypt': z=decryptLeaf(userInput[x],refKey,cryptKey)
		outputText=str(outputText)+str(z)
		if action=='encrypt':staticText=outputText
	return outputText

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
		if command == 'k' or command == 'key':
			return 'key'
		elif command == 'e' or command == 'encrypt':
			return 'encrypt'
		elif command == 'd' or command == 'decrypt':
			return 'decrypt'
		elif command == 'q' or command == 'quit' or command == 'exit':
			return 'quit'
		else:
			print("\""+command+"\" bad input. Try again.")
			continue

def task(selected_task):
	if selected_task == 'key':
		acceptKey()
	elif selected_task == 'encrypt':
		userPlaintext = str(input("Enter plaintext to be encrypted: "))
		encryptedText=downstream(userPlaintext,'encrypt')
		print("Encryption complete: "+encryptedText)
	elif selected_task == 'decrypt':
		userCiphertext = str(input("Enter ciphertext to be decrypted: "))
		decryptedText=downstream(userCiphertext,'decrypt')
		print("Decryption complete: "+decryptedText)
	elif selected_task == 'quit':
		global T
		T = 1

greeting()
T = 0
while T == 0:
	choice = get_command()
	task(choice)
