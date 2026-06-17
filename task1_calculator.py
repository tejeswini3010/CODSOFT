number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: \n"))

#choosing
print("Choose the operation you want to perform: \n")
print("1. Addition \n")
print("2. Subtraction \n")  
print("3. Multiplication \n")
print("4. Division \n") 
print("5. Modulus division \n")

choice=input("Enter your choice: \n")

if choice=="1":
    print("The addition of the two numbers is: \n", number1+number2)

elif choice=="2":
    print("The subtraction of the two numbers is: \n", number1-number2)

elif choice=="3":
    print("The multiplication of the two numbers is: \n", number1*number2)

elif choice=="4":
    if number2!=0:
        print("The division of the two numbers is: ", number1/number2)
    else:
        print("Division by zero is not allowed.\n")

elif choice=="5":
    if number2!=0:
        print("The modulus division of the two numbers is: ", number1%number2)
    else:
        print("Modulus division by zero is not allowed.\n")

else:
    print("Invalid choice. Please select a valid operation that is from above.\n")
