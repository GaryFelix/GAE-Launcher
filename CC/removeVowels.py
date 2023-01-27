words = "Gary"

print("Original word : ",words)

vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ""

for i in range(len(words)):
    if words[i] not in vowels:
        result+=words[i]
        
print("After removing vowels : ",result)