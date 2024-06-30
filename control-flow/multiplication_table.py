number= int(input("Enter a number to see its multiplication table: "))
for i in range(10):
    r=number*(i+1)
    print(f"{number}*{i+1}={r}")