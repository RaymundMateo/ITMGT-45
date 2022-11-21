def vigenere_cipher(message, key):
    key = list(key)
    
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(message, key):
	cipher_text = []
	for i in range(len(message)):
		x = (ord(message[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

string = "JOBEN"
keyword = "ITE"
key = vigenere_cipher(string, keyword)
cipher_text = cipherText(string,key)
print("Vigenere Cipher Text :", cipher_text)

