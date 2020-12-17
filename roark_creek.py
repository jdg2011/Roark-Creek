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
import configparser
config=configparser.ConfigParser()
config.read('config.ini')
import pyperclip
import math
import time
import secrets
import datetime
from itertools import product
version_number="2.0.0-beta005"
keyBase='nKi+T?d&OqAk<Y,4!SP-NZf[\E1MU/JwxHIsR@{r})Lvj]7(~mz0BV#y6tu:%3XGFbD;l.89C*$|^o5ga=Qc>peh2W'
firstNinetyPrimes=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463)

def printGreeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek "+version_number+"    |\n|               \"Bufflehead\"              |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit [h]elp")
	if config['defaultKey']['UseDefaultKey']=='True':
		processKey(config['defaultKey']['KeyValue'])
	keyEntered=True

def processKey(keyString):
	if len(keyString)!=24:
		print("Error! Key must be exactly 24 characters long.")
		return 0
	else:
		global keyBit
		keyBit=[]
		for x in keyString: keyBit.append(firstNinetyPrimes[keyBase.index(x)])
		global keyHash_cryptMult1
		keyHash_cryptMult1=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5]+keyBit[6]*keyBit[7]+keyBit[8]*keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]*keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]*keyBit[21]+keyBit[22]*keyBit[23],1010))
		global keyHash_cryptMult2
		keyHash_cryptMult2=int(math.fmod(keyBit[6]*keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23]+keyBit[0]+keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5],1010))
		global keyHash_refMult1
		keyHash_refMult1=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],1010))
		global keyHash_refMult2
		keyHash_refMult2=int(math.fmod(keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23]*keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5],1010))
		keyHash_leafBook=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1010))
		keyHash_seed1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7],98))
		keyHash_seed2=int(math.fmod(keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15],98))
		keyHash_seed3=int(math.fmod(keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],98))
		keyHash_seed4=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7],98))
		keyHash_seed5=int(math.fmod(keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15],98))
		keyHash_seed6=int(math.fmod(keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],98))
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
		global seedDict
		seedDict={}
		seedDict.update({'seed1':seedBook1[keyHash_seed1]})
		seedDict.update({'seed2':seedBook2[keyHash_seed2]})
		seedDict.update({'seed3':seedBook1[keyHash_seed3]})
		seedDict.update({'seed4':seedBook2[keyHash_seed4]})
		seedDict.update({'seed5':seedBook1[keyHash_seed5]})
		seedDict.update({'seed6':seedBook2[keyHash_seed6]})
		global keyEntered
		keyEntered=True
		return 1

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
	kTp=0
	for x in range(len(inputText)):
		if i==0:
			p1=seedDict['seed1']
			p2=seedDict['seed2']
			p3=seedDict['seed3']
		elif i==1:
			p1=seedDict['seed2']
			p2=seedDict['seed3']
			p3=staticText[x-1]
		elif i==2:
			p1=seedDict['seed3']
			p2=staticText[x-1]
			p3=staticText[x-2]
		else:
			p1=staticText[x-1]
			p2=staticText[x-2]
			p3=staticText[x-3]
		i+=1
		kTp+=1
		if kT>23: kT=0
		refKey=math.fmod((findLeafValue(p1)*findLeafValue(p2)*findLeafValue(p3)*keyHash_refMult1)*(keyBit[kT]+kTp),1010)
		cryptKey=math.fmod((findLeafValue(p1)+findLeafValue(p2)+findLeafValue(p3)*keyHash_cryptMult1)+(keyBit[kT]+kTp),1010)
		if action=='encrypt': z=encryptText(inputText[x],refKey,cryptKey,'1')
		if action=='decrypt': z=decryptText(inputText[x],refKey,cryptKey,'1')
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
	kTp=0
	for x in range(len(inputText)):
		if i==0:
			p1=seedDict['seed4']
			p2=seedDict['seed5']
			p3=seedDict['seed6']
		elif i==1:
			p1=seedDict['seed5']
			p2=seedDict['seed6']
			p3=staticText[x-1]
		elif i==2:
			p1=seedDict['seed6']
			p2=staticText[x-1]
			p3=staticText[x-2]
		else:
			p1=staticText[x-1]
			p2=staticText[x-2]
			p3=staticText[x-3]
		i+=1
		if kT>23:
			kT=0
			kTp+=1
		refKey=math.fmod((findLeafValue(p1)*findLeafValue(p2)*findLeafValue(p3)*keyHash_refMult2)+(keyBit[kT]+kTp),1010)
		cryptKey=math.fmod((findLeafValue(p1)+findLeafValue(p2)+findLeafValue(p3)*keyHash_cryptMult2)+(keyBit[kT]+kTp),1010)
		if action=='encrypt': z=encryptText(inputText[x],refKey,cryptKey,'2')
		if action=='decrypt': z=decryptText(inputText[x],refKey,cryptKey,'2')
		outputText=str(outputText)+str(z)
		if action=='encrypt':staticText=outputText
		kT+=1
	return outputText

def encryptText(text,leafKey1,leafKey2,sequence):
	refBook=findNewBook(leafKey1,'ref'+sequence)
	cryptBook=findNewBook(leafKey2,'crypt'+sequence)
	refNum=refBook.index(text)
	output=cryptBook[refNum]
	return output

def decryptText(text,leafKey1,leafKey2,sequence):
	refBook=findNewBook(leafKey1,'ref'+sequence)
	cryptBook=findNewBook(leafKey2,'crypt'+sequence)
	cryptNum=cryptBook.index(text)
	output=refBook[cryptNum]
	return output

def findNewBook(leafKey,library):
	openLib=open('libraries/'+library+'.txt','r',encoding='utf8')
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

def findLeafValue(leaf):
	hashProduct=leafBook.index(leaf)
	return hashProduct

def generateRandomKey():
	keyString=''
	for x in range(24):
		keyBit=secrets.choice(keyBase)
		keyString=keyString+keyBit
	return keyString

def convertTuple(tup):
	str=''.join(tup)
	return str

def snagFish(ciphertext,target):
	attackLog=open('snagFishLog.txt','w',encoding='utf8')
	attackLog.write(str(datetime.datetime.now())+" Initiating snagFish attack...\r")
	attackLog.close()
	attemptNumber=0
	cartesianKey = product(config['snagFish']['KeyString'],repeat=24)
	print("SnagFish attack started. This will take time, depending on your CPU and the length of your ciphertext...")
	snagClock=0
	ClockInt=int(config['snagFish']['ClockingInterval'])
	for i in cartesianKey:
		if snagClock==0: tic=time.perf_counter()
		attemptNumber+=1
		keyGuess=convertTuple(i)
		processKey(keyGuess)
		attempt=processString(ciphertext,'decrypt')
		if option1 == 'v': print(">"+str(attemptNumber)+" key "+keyGuess+" results: "+attempt)
		if target in attempt:
			attackLog=open('snagFishLog.txt','a')
			attackLog.write(str(datetime.datetime.now())+" Successfully found target: "+attempt+"\rAttempt number: "+str(attemptNumber)+"\rKey used: "+keyGuess)
			attackLog.close()
			print("Success!")
			break
		if snagClock==ClockInt:
			toc=time.perf_counter()
			rate=round(ClockInt/(toc-tic),1)
			if option1 != 'v': print("(Attempting "+str(rate)+" keys per second)")
			snagClock=0
		else:
			snagClock+=1

def flyFish(ciphertext,attemptNumber):
	attackLog=open('flyFishLog.txt','w',encoding='utf8')
	attackLog.write(str(datetime.datetime.now())+" Initiating flyFish attack...\r")
	print("FlyFish attack started. This will take time, depending on the length of your ciphertext and number of attempts...")
	flyClock=0
	ClockInt=int(config['flyFish']['ClockingInterval'])
	for x in range(int(attemptNumber)):
		keyGuess=generateRandomKey()
		if flyClock==0: tic=time.perf_counter()
		processKey(keyGuess)
		attempt=processString(ciphertext,'decrypt')
		attackLog.write(str(datetime.datetime.now())+" Attempt #"+str(x)+": key "+keyGuess+" results: "+attempt+"\r")
		if flyClock==1000:
			toc=time.perf_counter()
			rate=round(1000/(toc-tic),1)
			print("(Attempting "+str(rate)+" keys per second)")
			flyClock=0
		else:
			flyClock+=1
	print("FlyFish attack complete. See flyFishLog.txt for results.")
	attackLog.close()

def printHelp():
	helpFile = open('help.txt','r')
	print(helpFile.read())
	helpFile.close()

def getCommand():
	global option1
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
		elif command == 'c' or command == 'copy': return 'copy'
		elif command == 's' or command == 'snagFish': return 'snag'
		elif command == 's -v' or command == 'snagFish -v':
			option1 = 'v'
			return 'snag'
		elif command == 'f' or command == 'flyFish': return 'fly'
		elif command == 'h' or command == 'help': return 'help'
		elif command == 'q' or command == 'quit' or command == 'exit': return 'quit'
		else:
			print("\""+command+"\" bad input. Try again.")
			continue

def runTask(selectedTask):
	global cache1
	if selectedTask=='key':
		userKey=input("Enter 24-bit key: ")
		check=processKey(userKey)
		if check==1:print("Key accepted.")
	elif selectedTask=='encrypt':
		encryptedText=processString(str(input("Enter plaintext to be encrypted: ")),'encrypt')
		print("Encryption complete:\n"+encryptedText)
		cache1=encryptedText
	elif selectedTask=='decrypt':
		decryptedText=processString(str(input("Enter ciphertext to be decrypted: ")),'decrypt')
		print("Decryption complete:\n"+decryptedText)
	elif selectedTask=='generate':
		print("Generating random key...")
		newKey=generateRandomKey()
		processKey(newKey)
		print("New key generated and in place:\n"+str(newKey))
	elif selectedTask=='copy':
		pyperclip.copy(cache1)
		print(cache1+" copied to clipboard")
	elif selectedTask=='snag':
		userInput=input("Enter ciphertext to attack: ")
		userTarget=input("Enter a target word or phrase: ")
		print("Initiating snagFish attack...")
		snagFish(userInput,userTarget)
	elif selectedTask=='fly':
		userInput=input("Enter ciphertext to attack: ")
		userAttempts=input("Enter number of guesses to attempt: ")
		try:
			attempts=int(userAttempts)
		except:
			print("Error! Number of guesses must be a whole number (e.g. 1000).")
		else:
			print("Initiating flyFish attack...")
			flyFish(userInput,userAttempts)
	elif selectedTask=='help': printHelp()
	elif selectedTask=='quit':
		global T
		T=1

keyEntered=False
printGreeting()
T = 0
while T == 0:
	option1 = 0
	runTask(getCommand())
