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
import os
import configparser
import pyperclip
import math
import time
import secrets
import datetime
from itertools import product
version_number="2.0.0-beta011"
keyBase='nKi+T?d&OqAk<Y,4!SP-NZf[\E1MU/JwxHIsR@{r})Lvj]7(~mz0BV#y6tu:%3XGFbD;l.89C*$|^o5ga=Qc>peh2W'
firstNinetyPrimes=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463)

def printGreeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek "+version_number+"    |\n|               \"Bufflehead\"              |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit [h]elp")
	if config['defaultKey']['UseDefaultKey']=='True':
		processKey(config['defaultKey']['KeyValue'])
	keyEntered=True

def generateConfigFile():
	config = configparser.ConfigParser()
	config['defaultKey'] = {}
	config['defaultKey']['UseDefaultKey'] = 'False'
	config['defaultKey']['KeyValue'] = 'ABCDEFGHIJKLMNOP12345678'
	config['snagFish'] = {}
	config['snagFish']['KeyString'] = 'eEaAsStToOiInNdDK+?&qk<Y,4!P-Zf[\1MU/JwxHR@{r})Lvj]7(~mz0BV#y6u:%%3XGFb;l.89C*$|^5g=Qc>ph2W'
	config['snagFish']['ClockingInterval'] = '1000'
	config['flyFish'] = {}
	config['flyFish']['ClockingInterval'] = '1000'
	with open('config.ini', 'w') as configfile:
		config.write(configfile)

def processKey(keyString):
	if len(keyString)!=24:
		print("Error! Key must be exactly 24 characters long.")
		return 0
	else:
		global keyBit
		keyBit=[]
		for x in keyString: keyBit.append(firstNinetyPrimes[keyBase.index(x)])
		global leafMultiplier
		leafMultiplier={
		'crypt1':int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5]+keyBit[6]*keyBit[7]+keyBit[8]*keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]*keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]*keyBit[21]+keyBit[22]*keyBit[23],1010)),
		#'crypt1':int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5]+keyBit[6],1010)),
		'crypt2':int(math.fmod(keyBit[6]*keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23]+keyBit[0]+keyBit[1]+keyBit[2]*keyBit[3]+keyBit[4]*keyBit[5],1010)),
		#'crypt2':int(math.fmod(keyBit[7]*keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13],1010)),
		#'crypt3':int(math.fmod(keyBit[14]*keyBit[15]+keyBit[16]*keyBit[17]+keyBit[18]*keyBit[19]+keyBit[20],1010)),
		#'crypt4':int(math.fmod(keyBit[21]*keyBit[22]+keyBit[23]*keyBit[24]+keyBit[25]*keyBit[26]+keyBit[27],1010)),
		'ref1':int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],1010)),
		'ref2':int(math.fmod(keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]*keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]*keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23]*keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]*keyBit[4]+keyBit[5],1010))
		#'ref1':int(math.fmod(keyBit[28]*keyBit[29]+keyBit[30]*keyBit[31]+keyBit[32]*keyBit[33]+keyBit[34],1010)),
		#'ref2':int(math.fmod(keyBit[35]*keyBit[36]+keyBit[37]*keyBit[38]+keyBit[39]*keyBit[40]+keyBit[41],1010)),
		#'ref3':int(math.fmod(keyBit[42]*keyBit[43]+keyBit[44]*keyBit[45]+keyBit[46]*keyBit[47]+keyBit[48],1010)),
		#'ref4':int(math.fmod(keyBit[49]*keyBit[50]+keyBit[51]*keyBit[52]+keyBit[53]*keyBit[54]+keyBit[55],1010)),
}
		keyHash_leafBook=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]*keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1010))
		#keyHash_leafBook=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]*keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]*keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23]+keyBit[24]+keyBit[25]+keyBit[26]+keyBit[27]+keyBit[28]*keyBit[29]+keyBit[30]+keyBit[31]+keyBit[32]+keyBit[33]+keyBit[34]+keyBit[35]*keyBit[36]+keyBit[37]+keyBit[38]+keyBit[39]+keyBit[40]+keyBit[41]+keyBit[42]*keyBit[43]+keyBit[44]+keyBit[45]+keyBit[46]+keyBit[47]+keyBit[48]+keyBit[49]*keyBit[50]+keyBit[51]+keyBit[52]+keyBit[53]+keyBit[54]+keyBit[55],1010))
		keyHash_seed1=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7],98))
		#keyHash_seed1=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]+keyBit[3]+keyBit[54]+keyBit[16],98))
		#keyHash_seed2=int(math.fmod(keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7]+keyBit[54]+keyBit[16],98))
		#keyHash_seed3=int(math.fmod(keyBit[8]+keyBit[9]+keyBit[10]*keyBit[12]+keyBit[49]+keyBit[16],98))
		#keyHash_seed4=int(math.fmod(keyBit[13]+keyBit[14]+keyBit[15]+keyBit[17]*keyBit[49]+keyBit[11],98))
		#keyHash_seed5=int(math.fmod(keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[41]*keyBit[11],98))
		#keyHash_seed6=int(math.fmod(keyBit[22]+keyBit[23]+keyBit[24]+keyBit[26]*keyBit[41]+keyBit[11],98))
		#keyHash_seed7=int(math.fmod(keyBit[28]+keyBit[29]+keyBit[30]*keyBit[31]+keyBit[34]+keyBit[11],98))
		#keyHash_seed8=int(math.fmod(keyBit[32]+keyBit[33]*keyBit[35]+keyBit[36]+keyBit[34]+keyBit[11],98))
		#keyHash_seed9=int(math.fmod(keyBit[37]*keyBit[38]+keyBit[39]+keyBit[40]+keyBit[27]+keyBit[11],98))
		#keyHash_seed10=int(math.fmod(keyBit[42]+keyBit[43]*keyBit[44]+keyBit[45]+keyBit[27]+keyBit[16],98))
		#keyHash_seed11=int(math.fmod(keyBit[46]+keyBit[47]+keyBit[48]*keyBit[50]+keyBit[25]+keyBit[16],98))
		#keyHash_seed12=int(math.fmod(keyBit[51]+keyBit[52]+keyBit[53]+keyBit[55]*keyBit[25]+keyBit[16],98))
		keyHash_seed2=int(math.fmod(keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15],98))
		keyHash_seed3=int(math.fmod(keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],98))
		keyHash_seed4=int(math.fmod(keyBit[0]+keyBit[1]*keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]*keyBit[6]+keyBit[7],98))
		keyHash_seed5=int(math.fmod(keyBit[8]+keyBit[9]*keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]*keyBit[14]+keyBit[15],98))
		keyHash_seed6=int(math.fmod(keyBit[16]+keyBit[17]*keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]*keyBit[22]+keyBit[23],98))
		#keyHash_seedBookA=int(math.fmod(keyBit[13]+keyBit[43]+keyBit[44]+keyBit[45]+keyBit[46]+keyBit[47]+keyBit[48]+keyBit[49]+keyBit[50]+keyBit[51]+keyBit[52]+keyBit[53]+keyBit[54]+keyBit[28],1010))
		#keyHash_seedBookB=int(math.fmod(keyBit[55]+keyBit[29]+keyBit[30]+keyBit[31]+keyBit[32]+keyBit[33]+keyBit[34]+keyBit[35]+keyBit[36]+keyBit[37]+keyBit[38]+keyBit[39]+keyBit[40]+keyBit[14],1010))
		#keyHash_seedBookC=int(math.fmod(keyBit[41]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23]+keyBit[24]+keyBit[25]+keyBit[26]+keyBit[0],1010))
		#keyHash_seedBookD=int(math.fmod(keyBit[27]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[42],1010))
		keyHash_seedBookA=int(math.fmod(keyBit[0]+keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]*keyBit[11]+keyBit[12]*keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]+keyBit[23],1010))
		keyHash_seedBookB=int(math.fmod(keyBit[0]*keyBit[1]+keyBit[2]+keyBit[3]+keyBit[4]+keyBit[5]+keyBit[6]+keyBit[7]+keyBit[8]+keyBit[9]+keyBit[10]+keyBit[11]+keyBit[12]+keyBit[13]+keyBit[14]+keyBit[15]+keyBit[16]+keyBit[17]+keyBit[18]+keyBit[19]+keyBit[20]+keyBit[21]+keyBit[22]*keyBit[23],1010))
		#keyHash_refBookLanding=int(math.fmod(keyBit[29]+keyBit[31]+keyBit[33]+keyBit[35]+keyBit[37]+keyBit[39]+keyBit[41],11))
		#keyHash_refBookVeterans=int(math.fmod(keyBit[43]+keyBit[45]+keyBit[47]+keyBit[49]+keyBit[51]+keyBit[53]+keyBit[55],11))
		#keyHash_refBookGretna=int(math.fmod(keyBit[0]+keyBit[2]+keyBit[4]+keyBit[6]+keyBit[8]+keyBit[10]+keyBit[12],11))
		#keyHash_refBookShepherd=int(math.fmod(keyBit[14]+keyBit[16]+keyBit[18]+keyBit[20]+keyBit[22]+keyBit[24]+keyBit[26],11))
		#keyHash_cryptBookLanding=int(math.fmod(keyBit[28]+keyBit[30]+keyBit[32]+keyBit[34]+keyBit[36]+keyBit[38]+keyBit[40],11))
		#keyHash_cryptBookVeterans=int(math.fmod(keyBit[42]+keyBit[44]+keyBit[46]+keyBit[48]+keyBit[50]+keyBit[52]+keyBit[54],11))
		#keyHash_cryptBookGretna=int(math.fmod(keyBit[1]+keyBit[3]+keyBit[5]+keyBit[7]+keyBit[9]+keyBit[11]+keyBit[13],11))
		#keyHash_cryptBookShepherd=int(math.fmod(keyBit[15]+keyBit[17]+keyBit[19]+keyBit[21]+keyBit[23]+keyBit[25]+keyBit[27],11))
		global leafBook
		leafBook=findNewBook(keyHash_leafBook,'leaf')
		seedBookA=findNewBook(keyHash_seedBookA,'seed')
		seedBookB=findNewBook(keyHash_seedBookB,'seed')
		#seedBookC=findNewBook(keyHash_seedBookC,'seed')
		#seedBookD=findNewBook(keyHash_seedBookD,'seed')
		global seedDict
		seedDict={
			'seed1':seedBookA[keyHash_seed1],
			'seed2':seedBookB[keyHash_seed2],
			'seed3':seedBookA[keyHash_seed3],
			'seed4':seedBookB[keyHash_seed4],
			'seed5':seedBookA[keyHash_seed5],
			'seed6':seedBookB[keyHash_seed6]
}
		# seedDict={
			# 'seed1':seedBookA[keyHash_seed1],
			# 'seed2':seedBookB[keyHash_seed2],
			# 'seed3':seedBookC[keyHash_seed3],
			# 'seed4':seedBookD[keyHash_seed4],
			# 'seed5':seedBookA[keyHash_seed5],
			# 'seed6':seedBookB[keyHash_seed6],
			# 'seed7':seedBookC[keyHash_seed7],
			# 'seed8':seedBookD[keyHash_seed8],
			# 'seed9':seedBookA[keyHash_seed9],
			# 'seed10':seedBookB[keyHash_seed10],
			# 'seed11':seedBookC[keyHash_seed11],
			# 'seed12':seedBookD[keyHash_seed12]
# }
		global keyEntered
		keyEntered=True
		return 1

def processString(string,action):
	ref_landing='(findLeafValue(leaf1)*findLeafValue(leaf2)*findLeafValue(leaf3)*leafMultiplier["ref1"])*(keyBit[kT]+kTp)'
	crypt_landing='(findLeafValue(leaf1)+findLeafValue(leaf2)+findLeafValue(leaf3)*leafMultiplier["crypt1"])+(keyBit[kT]+kTp)'
	ref_veterans='(findLeafValue(leaf1)*findLeafValue(leaf2)*findLeafValue(leaf3)*leafMultiplier["ref2"])+(keyBit[kT]+kTp)'
	crypt_veterans='(findLeafValue(leaf1)+findLeafValue(leaf2)*findLeafValue(leaf3)+leafMultiplier["crypt2"])+(keyBit[kT]+kTp)'
	ref_gretna='(findLeafValue(leaf1)*findLeafValue(leaf2)*findLeafValue(leaf3)+leafMultiplier["ref3"])*(keyBit[kT]+kTp)'
	crypt_gretna='(findLeafValue(leaf1)*findLeafValue(leaf2)+findLeafValue(leaf3)+leafMultiplier["crypt3"])+(keyBit[kT]+kTp)'
	ref_shepherd='(findLeafValue(leaf1)*findLeafValue(leaf2)+findLeafValue(leaf3)*leafMultiplier["ref4"])*(keyBit[kT]+kTp)'
	crypt_shepherd='(findLeafValue(leaf1)+findLeafValue(leaf2)+findLeafValue(leaf3)+leafMultiplier["crypt4"])*(keyBit[kT]+kTp)'
	if action=='encrypt':
		x=stream(string,action,'seed1','seed2','seed3',ref_landing,crypt_landing)
		finalText=stream(x[::-1],action,'seed4','seed5','seed6',ref_veterans,crypt_veterans)
	elif action=='decrypt':
		x=stream(string,action,'seed4','seed5','seed6',ref_veterans,crypt_veterans)
		finalText=stream(x[::-1],action,'seed1','seed2','seed3',ref_landing,crypt_landing)
	return finalText

def stream(inputText,action,seedA,seedB,seedC,expressionRefKey,expressionCryptKey):
	outputText=""
	if action=='decrypt':staticText=inputText
	global keyBit
	i=0
	kT=0
	kTp=0
	for x in range(len(inputText)):
		if i==0:
			leaf1=seedDict[seedA]
			leaf2=seedDict[seedB]
			leaf3=seedDict[seedC]
		elif i==1:
			leaf1=seedDict[seedB]
			leaf2=seedDict[seedC]
			leaf3=staticText[x-1]
		elif i==2:
			leaf1=seedDict[seedC]
			leaf2=staticText[x-1]
			leaf3=staticText[x-2]
		else:
			leaf1=staticText[x-1]
			leaf2=staticText[x-2]
			leaf3=staticText[x-3]
		i+=1
		kTp+=1
		if kT>23: kT=0
		refKey=math.fmod(eval(expressionRefKey),1010)
		cryptKey=math.fmod(eval(expressionCryptKey),1010)
		if action=='encrypt': z=encryptText(inputText[x],refKey,cryptKey,'1')
		if action=='decrypt': z=decryptText(inputText[x],refKey,cryptKey,'1')
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

if bool(os.path.exists('config.ini')) is False: generateConfigFile()
config=configparser.ConfigParser()
config.read('config.ini')
keyEntered=False
printGreeting()
T = 0
while T == 0:
	option1 = 0
	runTask(getCommand())
