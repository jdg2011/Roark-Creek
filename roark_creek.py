#-------------------------------------------------------------------------------
# Name:        Roark Creek
# Purpose:     To deliver secure stream encryption through use of a symmetrical key.
#
# Author:      Jordan Gloor
#
# Created:     25/08/2020
# Copyright:   (c) Jordan Gloor 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Notes
	#A "sub-string not found" error typically means you used a character not included in the libraries.
	#Need error handling for unacceptable keys and the like
	#Need to gain the ability to rotate through books as the stream progresses
import math
#libraries
version_number = "0.0.1"
cryptLib=open('cryptLib1.txt','rb')
refLib=open('readLib1.txt','rb')
keyHashLib='mHUa_?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z'
#lists for processing text
ptList=[]
cryptList=[]
ctList=[]
decryptList=[]
seed = "A"
#In the future this^ should be a variable defined by the key

def greeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek v1.0             |\n|              \"Albatross\"               |\n|                                         |\n-------------------------------------------")
	print("\nCommands: [k]ey [e]ncrypt [d]ecrypt [q]uit")
def acceptKey():
	userKey=input("Enter 4-bit key: ")
	print("Hashing key and finding books...")
	keyBit0=keyHashLib.index(userKey[0])
	keyBit1=keyHashLib.index(userKey[1])
	keyBit2=keyHashLib.index(userKey[2])
	keyBit3=keyHashLib.index(userKey[3])
	keyHash_cryptBook=int(math.fmod(keyBit0*keyBit1+keyBit2*keyBit3,30))
	keyHash_refBook=int(math.fmod(keyBit0+keyBit1*keyBit2+keyBit3,30))
	i=0
	for x in cryptLib:
		if i == keyHash_cryptBook:
			global chosenCryptBook
			chosenCryptBook=str(cryptLib.readline())
			#print("The chosen cryptographic book is: "+chosenCryptBook)
			break
		else:
			i+=1
			continue
	i=0
	for x in refLib:
		if i == keyHash_refBook:
			global chosenRefBook
			chosenRefBook = str(refLib.readline())
			#print("The chosen reference book is: "+chosenRefBook)
			break
		else:
			i+=1
			continue
	print("Key accepted: "+str(userKey))

def encryptAries():
	#assigns numerical value for each character in given plaintext, storing them in the ptList
	userPlaintext = str(input("Enter plaintext to be encrypted: "))
	print("\nProcessing plaintext...")
	i = 0
	for x in range(len(userPlaintext)):
		parse = chosenRefBook.index(userPlaintext[i])
		ptList.append(parse)
		i += 1
	print("Plaintext accepted: "+userPlaintext)
	#print(ptList)
	#loops through the numerical values stored in ptList, finds the cooresponding characters in the chosen cryptographic library, and stores the found characters in cryptList
	print("\nEncrypting plaintext...")
	for x in ptList:
		parse = chosenCryptBook[x]
		cryptList.append(parse)
	print("Encryption complete.")
	print(cryptList)
	#loops through the characters stored in cryptList and prints them in a string
	sep = ""
	for x in cryptList:
		encryptedText = sep.join(cryptList)
	print("Here's your encrypted text: "+encryptedText)

def decryptAries():
	userCiphertext = str(input("Enter ciphertext to be decrypted: "))
	print("\nProcessing ciphertext...")
	i = 0
	for x in range(len(userCiphertext)):
		parse = chosenCryptBook.index(userCiphertext[i])
		ctList.append(parse)
		i += 1
	print("Ciphertext accepted: "+userCiphertext)
	#print(ctList)
	print("\nDecrypting ciphertext...")
	for x in ctList:
		parse = chosenRefBook[x]
		decryptList.append(parse)
	print("Decryption complete.")
	#print(decryptList)
	sep = ""
	for x in decryptList:
		decryptedText = sep.join(decryptList)
	print("Here's your decrypted text: "+decryptedText)

def downstreamDecryptAlbatross():
	userCiphertext = str(input("Enter ciphertext to be decrypted: "))
	decryptedText=""
	i=0
	for x in range(len(userCiphertext)):
		if i==0:
			p=seed
		else:
			p=userCiphertext[x-1]
		z=decryptAlbatross(userCiphertext[x],p)
		decryptedText=str(decryptedText)+str(z)
	print("Decryption complete: "+decryptedText)

def decryptAlbatross(leaf,preLeaf):
	preLeafNum=chosenRefBook.index(preLeaf)
	#This variable should be used to change the current RefBook
	cryptNum=chosenCryptBook.index(leaf)
	output=chosenRefBook[cryptNum]
	return output

def downstreamEncryptAlbatross():
	userPlaintext = str(input("Enter plaintext to be encrypted: "))
	encryptedText=""
	i=0
	for x in range(len(userPlaintext)):
		if i==0:
			p=seed
		else:
			p=encryptedText[x-1]
		z=encryptAlbatross(userPlaintext[x],p)
		encryptedText=str(encryptedText)+str(z)
	print("Encryption complete: "+encryptedText)

def encryptAlbatross(leaf,preLeaf):
	preLeafNum=chosenRefBook.index(preLeaf)
	#This variable should be used to change the current RefBook
	refNum=chosenRefBook.index(leaf)
	output=chosenCryptBook[refNum]
	return output

def get_command():
	x = 0
	while x == 0:
		command = str(input("\nEnter command: "))
		if command == "k" or command == "key":
			return "key"
		elif command == "e" or command == "encrypt":
			return "encrypt"
		elif command == "e2" or command == "encrypt2":
			return "encrypt2"
		elif command == "d" or command == "decrypt":
			return "decrypt"
		elif command == "d2" or command == "decrypt2":
			return "decrypt2"
		elif command == "q" or command == "quit":
			return "quit"
		else:
			print("\""+command+"\" bad input. Try again.")
			continue

def task(selected_task):
	if selected_task == "key":
		acceptKey()
	elif selected_task == "encrypt":
		encryptAries()
	elif selected_task == "encrypt2":
		downstreamEncryptAlbatross()
	elif selected_task == "decrypt":
		decryptAries()
	elif selected_task == "decrypt2":
		downstreamDecryptAlbatross()
	elif selected_task == "quit":
		global T
		T = 1

greeting()
T = 0
while T == 0:
	choice = get_command()
	task(choice)
cryptLib.close()
refLib.close()
