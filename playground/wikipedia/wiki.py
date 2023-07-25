import wikipedia
ba = wikipedia.search("Barack")
ba = wikipedia.summary("Barack", sentences=1)
print(ba)