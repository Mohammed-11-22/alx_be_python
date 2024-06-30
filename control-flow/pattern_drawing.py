n=int(input("Enter the size of the pattern: "))
i=0
while i<n:
    j=0
    while j<n:
        print("*", end="")
        j+=1
    print()
    i+=1