def reverse(str):
  reversed = ''
  for char in str:
    reversed = char + reversed
  return reversed

if __name__ == '__main__':
  print(reverse('hello world'))