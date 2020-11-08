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
version_number = "0.0.1d"
cryptLib=open('cryptLib1.txt','r')
keyHashLib='mHUa_?6|@xe>G7i}WNf.TER%zk=#nJovq:5DYXuV2BscAlb+F*3-$<{Q8ñy9(!~ÑL&4P^COgSt,`r0hpIdK wjM)1Z'
#lists for processing text
seed = "A"
#In the future this^ should be a variable defined by the key

def greeting():
	print("-------------------------------------------\n|                                         |\n|            Roark Creek v1.0             |\n|              \"Albatross\"                |\n|                                         |\n-------------------------------------------")
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
	keyHash_leafBook=int(math.fmod(keyBit0*keyBit3,30))
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
	cryptLib.close()
	i=0
	refLib=open('readLib1.txt','r')
	for x in refLib:
		if i == keyHash_refBook:
			global initialRefBook
			initialRefBook = str(refLib.readline())
			#print("The chosen reference book is: "+initialRefBook)
			break
		else:
			i+=1
			continue
	refLib.close()
	leafLib=open('leafLib1.txt', 'r')
	i=0
	for x in leafLib:
		if i == keyHash_leafBook:
			global leafRefBook
			leafRefBook = str(leafLib.readline())
			break
		else:
			i+=1
			continue
	leafLib.close()
	print("Key accepted: "+str(userKey))

def downstreamDecrypt():
	userCiphertext = str(input("Enter ciphertext to be decrypted: "))
	decryptedText=""
	i=0
	for x in range(len(userCiphertext)):
		if i==0:
			p=seed
		else:
			p=userCiphertext[x-1]
		i+=1
		preLeafNum=hashLeaf(p)
		z=decryptLeaf(userCiphertext[x],preLeafNum)
		decryptedText=str(decryptedText)+str(z)
	print("Decryption complete: "+decryptedText)

def decryptLeaf(leaf,preLeafNum):
	refLib=open('readLib1.txt','r')
	i=0
	for x in refLib:
		if i==preLeafNum:
			dRefBook=str(refLib.readline())
			break
		else:
			i+=1
			continue
	refLib.close()
	cryptNum=chosenCryptBook.index(leaf)
	output=dRefBook[cryptNum]
	return output

def hashLeaf(leaf):
	hashProduct=leafRefBook.index(leaf)
	return hashProduct

def downstreamEncrypt():
	userPlaintext = str(input("Enter plaintext to be encrypted: "))
	encryptedText=""
	i=0
	for x in range(len(userPlaintext)):
		if i==0:
			p=seed
		else:
			p=encryptedText[x-1]
		i+=1
		preLeafNum=hashLeaf(p)
		z=encryptLeaf(userPlaintext[x],preLeafNum)
		encryptedText=str(encryptedText)+str(z)
	print("Encryption complete: "+encryptedText)

def encryptLeaf(leaf,preLeafNum):
	refLib=open('readLib1.txt','r')
	i=0
	for x in refLib:
		if i==preLeafNum:
			eRefBook=str(refLib.readline())
			break
		else:
			i+=1
			continue
	refLib.close()
	refNum=eRefBook.index(leaf)
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
