# def repeated_word(input_string):
#     # Remove special characters and convert the input string to lowercase
#     cleaned_string = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in input_string)
#     print(cleaned_string)

#     # Split the string into words
#     words = cleaned_string.split()

#     # Create a dictionary to store word occurrences
#     word_count = {}

#     # Traverse through each word and count its occurrences
#     for word in words:
#         if word in word_count:
#             return word  # Return the first repeated word
#         word_count[word] = 1

#     return None  # If no repeated words are found

# # Test the function
# input_string = "apple Apple"
# result = repeated_word(input_string)
# print("First repeated word:", result)

from hashtable import Hashtable

# Write a function called repeated word that finds the first word to occur more than once in a string
# Arguments: string
# Return: string
def first_repeated_word(string):
  # create a hashtable
  hashtable = Hashtable()
  # split the string into an array of words
  words = string.split()
  print(words)
  # iterate over the words
  for word in words:
    # if the word is in the hashtable
    if hashtable.contains(word):
      # return the word
      return word
    # else
    else:
      # add the word to the hashtable
      hashtable.set(word, word)
  # return None
  return None

if __name__ == "__main__":
  print(first_repeated_word("Once upon a time, there was a brave princess who..."))
  print(first_repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief..."))
  print(first_repeated_word("It was a queer, sultry summer, the summer they electrocuted me, and I didn't realize I was dead yet..."))