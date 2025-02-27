def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return 'Error: Division by zero'
    else:
        return a/b

print("Select operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    try:
        choice = int(input("Enter choice(1/2/3/4): "))
        if not 1<=choice<=4:
            raise ValueError
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if choice == 1:
            print(number_1,"+",number_2,"=",add(number_1,number_2))
        elif choice == 2:
            print(number_1,"-",number_2,"=",subtract(number_1,number_2))
        elif choice == 3:
            print(number_1,"*",number_2,"=",multiply(number_1,number_2))
        elif choice == 4:
            print(number_1,"/",number_2,"=",divide(number_1,number_2))

    except ValueError:
        print("Invalid input")