s="this is string example"

words = s.split()

result =[]

for word in words:
    result.append("".join(reversed(word)))

print(" ".join(result))    
# word_reverse = " ".join(word[::-1] for word in s.split())
# print("\n2) Word-wise reverse:")
# print(word_reverse)