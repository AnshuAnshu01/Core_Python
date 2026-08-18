s="this is string example"
result=""
for i in range (0,len(s),2):
    pair=s[i:i+2]

    if len(pair)==2:
        result += pair[1] + pair[0]
    else:
        result += pair
print(result)            