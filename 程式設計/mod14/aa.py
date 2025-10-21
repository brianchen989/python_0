# Function definition
def printinfo(*va):
    print('Output is: ')
    print(*va)
    for i in va:
        print(i)
    print()
# Call function
printinfo(10)
printinfo(70, 60, 50)