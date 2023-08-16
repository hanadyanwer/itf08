def sum ():
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"{n1}+{n2} :", n1+n2)

def subtraction ():
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(f"subtraction :", n1 - n2)

def multiplication ():
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print("multipication :", n1 * n2)

def division ():
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print("division :", n1 / n2)

def triangle_area():
    base = int(input("Enter the base"))
    length = int(input("Enter the length"))
    print("triangle_area :", 0.5*base*length)

def rectangle_area():
    length = int(input("Enter the length"))
    width = int(input("Enter the width"))
    print("rectangle_area :", length*width)

def circle_area():
    raduis = int(input("Enter the raduis"))
    print("circle_area :", 3.14*raduis*raduis)

while True :
    print("1. Sum\n"
"2. Subtract\n"
"3. Multiply\n"
"4. Division\n"
"5. Calculate triangle area\n"
"6. Calculate circle area\n"
"7. Calculate rectangle area\n"
"8. Exit\n")
    choice = int(input("Enter youre choice"))
    while True:
        if choice <=8 and choice >=1:
            break
        else:
            choice=int(input("Invalid input,Enter valid choice"))
    if choice == 1:
        sum()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        triangle_area()
    elif choice == 6:
        rectangle_area()
    elif choice == 7:
        circle_area()
    elif choice == 8:
        print("pye")
        exit()







