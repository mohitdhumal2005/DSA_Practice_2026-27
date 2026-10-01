sentence = input("Enter The sentence: ")
print("Original Sentence: ",sentence)

words = sentence.split()
print("Splitted Sentence into words: ",words)

for i in range(len(words)):
    words[i]=words[i][::-1]
print("Reversed words: ",words)

result = " ".join(words)
print("Reversed Sentence: ",result)