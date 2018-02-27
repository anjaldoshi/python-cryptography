import hashlib

password = input("Enter the password: ")
password = password.encode("utf8")

hash_pass = hashlib.sha224(password).hexdigest() #Hashing the password to 224 bits
hash_pass = bin(int(hash_pass, 16))[2:].zfill(8)
hash_pass = hash_pass[0:192] #truncating the hashed password to 48 hexdata (192 bits)

fo = open("keyfile.txt","w")
fo.write(hash_pass)	#Saving the key in a file
