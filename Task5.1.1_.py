values = input("Enter values separated by comma: ")

str_list = []
int_list = []

# Split input using comma
values = values.split(",")

# Check each value
for value in values:

    value = value.strip()

    if value.isdigit():
        int_list.append(int(value))

    else:
        str_list.append(value)


# Display integer list
print("Integer List:", int_list)

# Minimum and Maximum
if len(int_list) > 0:
    print("Minimum:", min(int_list))
    print("Maximum:", max(int_list))


# Display string list
print("String List:", str_list)

# Reverse string list
str_list.reverse()

print("Reversed String List:", str_list)