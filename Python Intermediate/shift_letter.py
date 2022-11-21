'''
def shift_letter(letter, shift):
    ans = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    X = sum(shift) % 26
    for i, c in enumerate(letter):
        index = ord(c) - ord('a')
        ans.append(chr(ord('a') + (index + X) % 26))
        X = (X - shift[i]) % 26

        return "".join(ans)
'''

def shift_letter(letter, shift):

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

print(shift_letter("A", 0))

