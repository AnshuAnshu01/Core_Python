row= int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for j in range(i):
        print(1 , end=" ")
    print()   

number=1
for i in range(1,row+1):
    for j in range(i):
        print(number,end=" ")
        number +=1
    print() 


for i  in range (row,0,-1):
    for j in range (i):
        print("*" , end=" ")
    print()     




for i in range(row):

    for j in range(row-i-1):
        print(" ",end="")

    for i in range(2*i+1):
        print("*",end="")
    print()            



for i in range(1,row+1):
        for j in range(row-1):
            print(" ",end="")
        for k in range(i):
            print("*",end=" ")
        print()   

for i in range(row-1,0,-1):
    for j in range(row-1):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()            



for i in range(1, row + 1):

    for j in range(row - i):
        print(" ", end="")

    for k in range(i):
        print("*", end=" ")

    print()

for i in range(row - 1, 0, -1):

    for j in range(row - i):
        print(" ", end="")

    for k in range(i):
        print("*", end=" ")

    print()
