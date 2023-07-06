from cypher.corpusLoader import word_list, name_list

# Create an encrypt function that takes in a plain text phrase and a numeric shift.
# the phrase will then be shifted that many letters.
# E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
# shifts that exceed 26 should wrap around.
# E.g. encrypt(‘abc’,27) would return ‘bcd’.
# shifts that push a letter out or range should wrap around.
# E.g. encrypt(‘zzz’,1) would return ‘aaa’.

def encrypt(plain_text, shift):
    encrypted_text = ""
    for letter in plain_text:
        if letter.isalpha():
            if letter.isupper():
                encrypted_text += chr((ord(letter) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(letter) + shift - 97) % 26 + 97)
        else:
            encrypted_text += letter
    return encrypted_text
  
#q: what is isalpha()?
#a: isalpha() is a built-in function used in string manipulations in python.
#q: what is isupper()?
#a: isupper() is a built-in function used in string manipulations in python.