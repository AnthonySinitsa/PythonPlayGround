def monthNam(list):
  for i, month in enumerate(list):
    print(f'{month} : {i + 1}')
  
if __name__ == "__main__":
  monthNam(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])