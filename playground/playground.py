def mult(str):
  newStr = ""
  for char in str:
    if char not in newStr:
      newStr += char
  return newStr

word = "commissioner"
print(mult(word))
print(mult("agressiveness"))

mult(word)