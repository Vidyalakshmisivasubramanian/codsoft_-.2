def calculator(a):
    s=int(input("Enter The Number 1:"))
    v=int(input("Enter The Number 2:"))
    if a==1:
        print("The addition of two numbers:",s+v)
    elif a==2:
        print("The subrtraction of two numbers:",s-v)
    elif a==3:
        print("The multiplication of two numbers:",s*v)
    elif a==4:
        print("The division of two numbers:",round(s/v,2))
    elif a==5:
        print("The exponentiation of two numbers:",s**v);  
    else:
        print("invalid number")


while True:
    print("\n\t\tCALCULATOR\nMenu:")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation")
    a=int(input("Enter The Choice(1,2,3,4,5):"))
    calculator(a)if a in [1,2,3,4,5] else print("Invalid Input..!")




