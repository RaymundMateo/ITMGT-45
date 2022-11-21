'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if (len(letter) > 1):
        return "Incorrect letter"
    elif (letter == " "):
        return " "
    elif (letter.isalpha() == False):
        return "Invalid character"

    if (isinstance(shift, int)) == False:
        shift = "Incorrect Input Number"
    
    while shift >= 26:
        shift -= 26

    ans = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    index_position = ans.index(letter)
    letter_shifter = ans[index_position + shift]

    return letter_shifter

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
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

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if (len(letter) > 1):
        return "Incorrect letter"
    elif (letter == " "):
        return " "
    elif (letter.isalpha() == False):
        return "Invalid character"
    
    if (len(letter_shift) > 1):
        return "Incorrect letter"
    elif (letter_shift == " "):
        return " "
    elif (letter_shift.isalpha() == False):
        return "Invalid character"

    ans = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letter_index_position = ans.index(letter)
    letter_shift_index_position = ans.index(letter_shift)
    added_index = letter_index_position + letter_shift_index_position
    
    if added_index >= 26:
        added_index -= 26

    x = ans[added_index]

    return x

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
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