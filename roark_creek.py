#-------------------------------------------------------------------------------
# Name:        Roark Creek
# Purpose:     To deliver secure stream encryption through use of a symmetrical key.
#
# Author:      Jordan Gloor
#
# Created:     08/25/2020
# Copyright:   (c) Jordan Gloor 2020
#-------------------------------------------------------------------------------

#Notes
	#A "sub-string not found" error typically means you used a character not included in the libraries.
import math
import random
import datetime
from itertools import product
version_number = "1.0.1a"

def greeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek "+version_number+"           |\n|                \"Albatross\"              |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit [h]elp")
	#Uncomment this to set a default key to save time when testing
	#processKey('111111111111111111111111')

def processKey(userKey):
	if len(userKey)!=24:
		print("Error! Key must be exactly 24 characters long.")
		return 0
	else:
		global keyBit
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
		global keyEntered
		keyEntered=True
		return 1

def findSeedValue(keyHash,library):
	i=0
	for x in library:
		if i==keyHash:
			seed=x
			break
		else:
			i+=1
			continue
	return seed

def processString(string,action):
	if action=='encrypt':
		x=downstream(string,action)
		finalText=upstream(x[::-1],action)
	elif action=='decrypt':
		x=upstream(string,action)
		finalText=downstream(x[::-1],action)
	return finalText

def downstream(inputText,action):
	outputText=""
	if action=='decrypt':staticText=inputText
	global keyBit
	i=0
	kT=0
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
		if kT>23: kT=0
		refKey=math.fmod(hashLeaf(p1)*hashLeaf(p2)*hashLeaf(p3)*keyHash_refMult1+keyBit[kT],1010)
		cryptKey=math.fmod(hashLeaf(p1)+hashLeaf(p2)+hashLeaf(p3)*keyHash_cryptMult1+keyBit[kT],1010)
		if action=='encrypt': z=encryptLeaf(inputText[x],refKey,cryptKey,'1')
		if action=='decrypt': z=decryptLeaf(inputText[x],refKey,cryptKey,'1')
		outputText=str(outputText)+str(z)
		if action=='encrypt':staticText=outputText
		kT+=1
	return outputText

def upstream(inputText,action):
	outputText=""
	if action=='decrypt':staticText=inputText
	global keyBit
	i=0
	kT=0
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
		if kT>23: kT=0
		refKey=math.fmod(hashLeaf(p1)*hashLeaf(p2)*hashLeaf(p3)*keyHash_refMult1+keyBit[kT],1010)
		cryptKey=math.fmod(hashLeaf(p1)+hashLeaf(p2)+hashLeaf(p3)*keyHash_cryptMult1+keyBit[kT],1010)
		if action=='encrypt': z=encryptLeaf(inputText[x],refKey,cryptKey,'2')
		if action=='decrypt': z=decryptLeaf(inputText[x],refKey,cryptKey,'2')
		outputText=str(outputText)+str(z)
		if action=='encrypt':staticText=outputText
		kT+=1
	return outputText

def encryptLeaf(leaf,leafKey1,leafKey2,sequence):
	refBook=findNewBook(leafKey1,'ref'+sequence)
	cryptBook=findNewBook(leafKey2,'crypt'+sequence)
	refNum=refBook.index(leaf)
	output=cryptBook[refNum]
	return output

def decryptLeaf(leaf,leafKey1,leafKey2,sequence):
	RefBook=findNewBook(leafKey1,'ref'+sequence)
	CryptBook=findNewBook(leafKey2,'crypt'+sequence)
	cryptNum=CryptBook.index(leaf)
	output=RefBook[cryptNum]
	return output

def findNewBook(leafKey,library):
	openLib=open('libraries/'+library+'.txt','r')
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

def convertTuple(tup):
	str=''.join(tup)
	return str

def genCart():
	perm = product('mHUa?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z', repeat = 24)
	for i in perm:
		output = convertTuple(i)
	return output

def snagFish(ciphertext,target):
	attackLog=open('snagFishLog.txt','w')
	attackLog.write(str(datetime.datetime.now())+" Beginning snagFish attack...\r")
	attackLog.close()
	y=0
	attemptNumber=0
	while y==0:
		cartesianKey = product('mHUa?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z', repeat = 24)
		for i in cartesianKey:
			attemptNumber+=1
			keyGuess=convertTuple(i)
			processKey(keyGuess)
			attempt=processString(ciphertext,'decrypt')
			print(">"+str(attemptNumber)+" key "+keyGuess+" results: "+attempt)
			if target in attempt:
				attackLog=open('snagFishLog.txt','a')
				attackLog.write(str(datetime.datetime.now())+" Successfully found target: "+attempt+"\rAttempt number: "+str(attemptNumber)+"\rKey used: "+keyGuess)
				attackLog.close()
				print("Success!")
				break
			continue

def printHelp():
	helpFile = open('help.txt','r')
	print(helpFile.read())
	helpFile.close()

def get_command():
	x = 0
	while x == 0:
		command = str(input("\nEnter command: "))
		if command == 'k' or command == 'key': return 'key'
		elif command == 'e' or command == 'encrypt':
			if keyEntered==True:
				return 'encrypt'
			else:
				print("No key entered. Use [k]ey or [g]enerate.")
				continue
		elif command == 'd' or command == 'decrypt':
			if keyEntered==True:
				return 'decrypt'
			else:
				print("No key entered. Use [k]ey or [g]enerate.")
				continue
		elif command == 'g' or command == 'generate': return 'generate'
		elif command == 's' or command == 'snagFish': return 'snag'
		elif command == 'h' or command == 'help': return 'help'
		elif command == 'q' or command == 'quit' or command == 'exit': return 'quit'
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
		encryptedText=processString(userPlaintext,'encrypt')
		print("Encryption complete: "+encryptedText)
	elif selected_task == 'decrypt':
		userCiphertext = str(input("Enter ciphertext to be decrypted: "))
		decryptedText=processString(userCiphertext,'decrypt')
		print("Decryption complete: "+decryptedText)
	elif selected_task == 'generate':
		print("Generating random key...")
		newKey=generateRandomKey()
		processKey(newKey)
		print("New key "+str(newKey)+" generated and in place.")
	elif selected_task == 'snag':
		userInput=input("Enter ciphertext to attack: ")
		userTarget=input("Enter a target word or phrase: ")
		print("Initiating snagFish attack...")
		snagFish(userInput,userTarget)
	elif selected_task == 'help':
		printHelp()
	elif selected_task == 'quit':
		global T
		T = 1

greeting()
T = 0
keyEntered=False
while T == 0:
	choice = get_command()
	task(choice)
