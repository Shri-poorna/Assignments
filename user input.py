start=int(input("Enter first no: "))
end=int(input("Enter the econd no: "))
for i in range(start,end+1):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
