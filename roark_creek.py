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
import random
import datetime
version_number = "0.2.6a"

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
		return 0
	else:
		print("Hashing key and finding books...")
		keyBit=[]
		keyHashLib='mHUa?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z'
		for x in userKey: keyBit.append(keyHashLib.index(x))
		global keyHash_cryptMult1
		keyHash_cryptMult1=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5]+keyBit[6]*keyBit[7]+keyBit[8]*keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]*keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]*keyBit[21]+keyBit[22]*keyBit[23],1010))
		global keyHash_cryptMult2
		keyHash_cryptMult2=int(math.fmod(keyBit[6]*keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23]+keyBit[0]+keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5],1010))
		global keyHash_refMult1
		keyHash_refMult1=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],1010))
		global keyHash_refMult2
		keyHash_refMult2=int(math.fmod(keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23]*keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5],1010))
		keyHash_leafBook=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1010))
		keyHash_seed1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7],91))
		keyHash_seed2=int(math.fmod(keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15],91))
		keyHash_seed3=int(math.fmod(keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],91))
		keyHash_seed4=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7],91))
		keyHash_seed5=int(math.fmod(keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15],91))
		keyHash_seed6=int(math.fmod(keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],91))
		keyHash_seedBook1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1010))
		keyHash_seedBook2=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23],1010))
		global leafBook
		leafBook=findNewBook(keyHash_leafBook,'leaf')
		seedBook1=findNewBook(keyHash_seedBook1,'seed')
		seedBook2=findNewBook(keyHash_seedBook2,'seed')
		seedBook3=findNewBook(keyHash_seedBook1,'seed')
		seedBook4=findNewBook(keyHash_seedBook1,'seed')
		seedBook5=findNewBook(keyHash_seedBook2,'seed')
		seedBook6=findNewBook(keyHash_seedBook1,'seed')
		global seed1
		seed1=findSeedValue(keyHash_seed1,seedBook1)
		global seed2
		seed2=findSeedValue(keyHash_seed2,seedBook2)
		global seed3
		seed3=findSeedValue(keyHash_seed3,seedBook1)
		global seed4
		seed4=findSeedValue(keyHash_seed4,seedBook1)
		global seed5
		seed5=findSeedValue(keyHash_seed5,seedBook2)
		global seed6
		seed6=findSeedValue(keyHash_seed6,seedBook1)
		return 1

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

def processString(string,action):
	if action=='encrypt':
		x=str(reversed(downstream(string,action)))
		finalText=upstream(x,action)
	elif action=='decrypt':
		x=str(reversed(upstream(string,action)))
		finalText=downstream(x,action)
	return finalText

def downstream(inputText,action):
	outputText=""
	if action=='decrypt':staticText=inputText
	i=0
	for x in range(len(inputText)):
		if i==0:
			p1=seed1
			p2=seed2
			p3=seed3
		elif i==1:
			p1=seed2
			p2=seed3
			p3=staticText[x-1]
		elif i==2:
			p1=seed3
			p2=staticText[x-1]
			p3=staticText[x-2]
		else:
			p1=staticText[x-1]
			p2=staticText[x-2]
			p3=staticText[x-3]
		i+=1
		refKey=math.fmod(hashLeaf(p1)*hashLeaf(p2)*hashLeaf(p3)*keyHash_refMult1,1010)
		cryptKey=math.fmod(hashLeaf(p1)+hashLeaf(p2)+hashLeaf(p3)*keyHash_cryptMult1,1010)
		if action=='encrypt': z=encryptLeaf(inputText[x],refKey,cryptKey)
		if action=='decrypt': z=decryptLeaf(inputText[x],refKey,cryptKey)
		outputText=str(outputText)+str(z)
		if action=='encrypt':staticText=outputText
	return outputText

def upstream(inputText,action):
	outputText=""
	if action=='decrypt':staticText=inputText
	i=0
	for x in range(len(inputText)):
		if i==0:
			p1=seed4
			p2=seed5
			p3=seed6
		elif i==1:
			p1=seed5
			p2=seed6
			p3=staticText[x-1]
		elif i==2:
			p1=seed6
			p2=staticText[x-1]
			p3=staticText[x-2]
		else:
			p1=staticText[x-1]
			p2=staticText[x-2]
			p3=staticText[x-3]
		i+=1
		refKey=math.fmod(hashLeaf(p1)*hashLeaf(p2)*hashLeaf(p3)*keyHash_refMult1,1010)
		cryptKey=math.fmod(hashLeaf(p1)+hashLeaf(p2)+hashLeaf(p3)*keyHash_cryptMult1,1010)
		if action=='encrypt': z=encryptLeaf(inputText[x],refKey,cryptKey)
		if action=='decrypt': z=decryptLeaf(inputText[x],refKey,cryptKey)
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

def generateRandomKey():
	keyString=''
	for x in range(24):
		keyBit=random.choice('mHUa?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z')
		keyString=keyString+keyBit
	return keyString

def bruteForceAttack(ciphertext):
	attackLog=open('attacklog.txt','w')
	attackLog.write(str(datetime.datetime.now())+" Beginning brute force attack...\r")
	y=0
	attemptNumber=0
	while y==0:
		attemptNumber+=1
		keyGuess=generateRandomKey()
		processKey(keyGuess)
		attempt=downstream(ciphertext,'decrypt')
		print("Attempt number "+str(attemptNumber)+": "+attempt)
		#Insert the text you're looking for in the decrypted output:
		if 'your target' in attempt:
			attackLog.write(str(datetime.datetime.now())+" Successfully found target: "+attempt+" on attempt number "+str(attemptNumber))
			attackLog.close()
			break
		continue

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
		elif command == 'g' or command == 'generate':
			return 'generate'
		elif command == 'b' or command == 'brute':
			return 'brute'
		elif command == 'q' or command == 'quit' or command == 'exit':
			return 'quit'
		else:
			print("\""+command+"\" bad input. Try again.")
			continue

def task(selected_task):
	if selected_task == 'key':
		userKey=input("Enter 24-bit key: ")
		check=processKey(userKey)
		if check==1:print("Key accepted: "+str(userKey))
	elif selected_task == 'encrypt':
		userPlaintext = str(input("Enter plaintext to be encrypted: "))
		encryptedText=downstream(userPlaintext,'encrypt')
		print("Encryption complete: "+encryptedText)
	elif selected_task == 'decrypt':
		userCiphertext = str(input("Enter ciphertext to be decrypted: "))
		decryptedText=downstream(userCiphertext,'decrypt')
		print("Decryption complete: "+decryptedText)
	elif selected_task == 'generate':
		print("Generating random key...")
		newKey=generateRandomKey()
		processKey(newKey)
		print("New key "+str(newKey)+" generated and in place.")
	elif selected_task == 'brute':
		userInput=input("Enter ciphertext to attack: ")
		print("Initiating brute force attack...")
		bruteForceAttack(userInput)
	elif selected_task == 'quit':
		global T
		T = 1

greeting()
T = 0
while T == 0:
	choice = get_command()
	task(choice)
