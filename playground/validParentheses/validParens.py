def isValid(s):

  stack = []
  mapping = {')' : '(', ']' : '[', '}' : '{'}

  for char in s:
    if char in mapping:
        if stack and stack[-1] == mapping[char]:
          stack.pop()
        else:
          return False
    else:
      stack.append(char)
  return True if not stack else False

s = "()[]{}"
print(isValid(s))