kent=[]
zuyg=[]
numbers = input("Enter a list of numbers separated by spaces: ").split()
for num in numbers:
    tiv=int(num)
    if tiv%2==0:
        zuyg.append(tiv)
    else:
        kent.append(tiv)
print("Even numbers:",kent,"\nOdd numbers:",zuyg)