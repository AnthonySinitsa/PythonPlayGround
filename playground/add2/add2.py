def add_2(list):
  for items in list:
    for i, num in enumerate(items):
      items[i] = num + 2
  return list

if __name__ == "__main__":
  print(add_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))