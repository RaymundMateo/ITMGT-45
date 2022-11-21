def shift_by_letter(letter, letter_shift):

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

print(shift_by_letter("B", "Z"))