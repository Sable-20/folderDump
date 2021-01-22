#DOESNT WORK


import base64

key = 'malware'

print("Provide the message you wish to encrypt via base64")
message = input()
enc = []
for i in range(len(message)):
	key_c = key[i % len(key)]
	enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
encryption = base64.urlsafe_b64encode("".join(enc).encode()).decode
print("Here is the decreypted message:\n"+encryption)

dec = []
message = base64.urlsafe_b64encode(encryption).decode()
for i in range(len(message)):
	key_c = key[i % len(key)]
	dec.append(chr((256+ ord(message[i]) - ord(key_c)) % 256))
print("Decrypted: \n" + "".join(dec))