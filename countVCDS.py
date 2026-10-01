string = input("Enter a String: ")
vowels=0
consonants=0
digits=0
special=0
for ch in string:
    if ch.isalpha():
        if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            vowels = vowels+1 
        else:
            consonants = consonants+1
    elif ch.isdigit():
        digits = digits+1
    else:
        special = special+1 
        
print("No. of Vowels: ",vowels)
print("No. of consonants: ",consonants)
print("No. of digits: ",digits)
print("No. of special character: ",special)
        