values=input("Enter values : ")
values=values.split(",")
int_list=[]
Str_list=[]
for value in values:
    value = value.strip()

    if value.isdigit():
        int_list.append(int(value))
    else:
        Str_list.append(value)


print(int_list)
print(max(int_list))
print(min(int_list))
print(Str_list)
print(Str_list[::-1])

