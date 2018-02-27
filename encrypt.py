#import

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
		34, 53, 46, 42, 50, 36, 29, 32]

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
	  63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
	 28, 29, 30, 31, 32, 1]

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
	 19, 13, 30, 6, 22, 11, 4, 25]

IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
		33, 1, 41, 9, 49, 17, 57, 25]

KSHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

#Open input file and read plain text
fo = open("inputfile.txt","r")
pt = fo.read()
fo.close()

#Open key file and read key
fo2 = open("keyfile.txt","r")
key = fo2.read()
fo2.close()

#Divide 192 bit key into 3 keys
key1 = key[0:64]
key2 = key[64:128]
key3 = key[128:192]
keys = []
padding = 0
ENCRYPT = 1
DECRYPT = 0

#Padding the input b
def addPadding(data):
	padlen = 8 - (len(data)%8)
	data += padlen * chr(padlen)
	plaintext = ''.join(bin(ord(x))[2:].zfill(8) for x in data)
	return plaintext

def remPadding(data):
	padlen = ord(data[-1])
	return data[:-padlen]

#Permuting data according to the table (Sbox, IP)
def permutation(block, table):
	j = []
	for i in table:
		j += block[i-1]
	x = ''.join(j)
	return x

#Exapnding data using Ebox
def expand(block, table):
	j = []
	for i in table:
		j += block[i-1]
	x = ''.join(j)
	return x

#Shift function for each round key
def keyshift(l,r,n):
	return l[n:]+l[:n], r[n:]+r[:n]

#Split data into equa; size blocks
def splitdata(data, n):
	blocks = [data[i:i+n] for i in range(0, len(data), n)]
	return blocks


#Generate round keys
def keygen(key):
	del keys[:]
	key = permutation(key, PC_1)
	l, r = key[0:28], key[28:56]

	for i in range(16):
		l, r = keyshift(l, r, KSHIFT[i])
		merge = l+r
		keys.append(permutation(merge, PC_2))

#Xor
def xor(r, k):
	x = []
	for i,j in zip(r,k):
		if( i == j ):
			x += '0'
		else:
			x += '1' 
	z = ''.join(x)
	return z

#Substituting bits uisng Sbox 
def substitute(x):
	subblocks = splitdata(x, 6)
	res = [] 
	for i in range(len(subblocks)):
		block = subblocks[i]
		row = int(block[0]+block[5], 2)
		column = int(''.join(block[1:][:-1]), 2)
		sval = S_BOX[i][row][column]
		val = bin(sval)[2:].zfill(4)
		res += val
	result = ''.join(res)
	return result


#Execution function for both encryption/decryption
def execute(key, plaintext, action, padding):
	
	if padding==1 and action==ENCRYPT:
		plaintext = addPadding(plaintext)
	else:
		plaintext = ''.join(bin(ord(x))[2:].zfill(8) for x in plaintext)	

	keygen(key)

	all_blocks = splitdata(plaintext,64)
	result = ""
	for block in all_blocks:
		block = permutation(block,IP)
		l, r = splitdata(block,32)
		temp = None

		#Round Function starts
		for i in range(16):
			rexp = expand(r, E)
			if action == ENCRYPT:
				temp = xor(rexp,keys[i])
			else:
				temp = xor(rexp,keys[15-i])
			temp = substitute(temp)
			temp = permutation(temp, P)
			temp = xor(l, temp)
			l = r
			r = temp
		result += permutation(r+l, IP_1)
	final_result = ''.join(chr(int(result[i:i+8], 2)) for i in range(0, len(result), 8))
	#return final_result
	if padding==1 and action==DECRYPT:
		return remPadding(final_result)
	else:
		return final_result

def encrypt(key, text, padding):
	return execute(key, text, ENCRYPT, padding)
    
def decrypt(key, text, padding):
	return execute(key, text, DECRYPT, padding)


#Execute 3DES
if len(pt)%8 !=0:
	padding = 1
else:
	padding = 0

cipher1 = encrypt(key1, pt, padding)
print(cipher1)
cipher2 = decrypt(key2, cipher1, 0)
print(cipher2)
ciphertext = encrypt(key3, cipher2, 0)
print(ciphertext)
ciphertext = ''.join(bin(ord(x))[2:].zfill(8) for x in ciphertext)
fo3 = open("cipher.txt","w")
fo3.write(ciphertext)
fo3.close


