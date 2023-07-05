def encrypt(plain_text, shift):
  encrypted_string = ''
  for char in plain_text:
    new_num = (int(char) + shift) % 10
    encrypted_string += str(new_num)
  return encrypted_string

def decrypt(encoded, shift):
  return encrypt(encoded, -shift)

if __name__ == "__main__":
  print(encrypt("8473", 3))
  print(decrypt("1706", 3))