def caesar_cipher(message, shift):
    result = ""
 
    for i in range(len(message)):
        char = message[i]
 
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
 
    return result
 
message = "ATTACKATONCE"
shift = 4
print ("Text  : " + message)
print ("Shift : " + str(shift))
print ("Cipher: " + caesar_cipher(message,shift))