s="this is string example"

words = s.split()

result =[]

for word in words:
    result.append("".join(reversed(word)))

print(" ".join(result))    