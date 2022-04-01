string = input("Paste input here: ").strip()

words = string.split(" ")  # breaking the string into individual words

for index, word in enumerate(words):
    words[index] = word.lower()

print("-".join(words))
