sentence = input("Enter A Sentence: ")
print("Original Sentence: ",sentence)

words = sentence.split()
print("Sentence Splitted into word: ",words)

longest = words[0]
shortest = words[0]

for ch in words:
    if len(ch) > len(longest):
        longest = ch
    if len(ch) < len(shortest):
        shortest = ch

print("Longest Word: ",longest)
print("Shortest Word: ",shortest)