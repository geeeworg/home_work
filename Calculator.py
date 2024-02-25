print("Select operation:| num")
print("               + |  1")
print("               - |  2")
print("               * |  3")
print("               / |  4")

while True:
    choice = int(input("Enter choice (1/2/3/4): "))

    if choice in (1,2,3,4):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", x+y)
        elif choice == 2:
            print("Result:", x-y)
        elif choice == 3:
            print("Result:", x*y)
        elif choice == 4 and y!=0:
            print("Result:", x/y)
        else:
            print("ERROR")
    else:
        print("Invalid input")
