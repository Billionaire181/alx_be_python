pattern = int(input("Enter the size of the pattern: "))
row = 0 
while row < pattern:
    row += 1
    for column in range(pattern):
        print("*", end="")
    print()
