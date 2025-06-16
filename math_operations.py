try:
    #take input from the user
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
    
    #Perform basic mathematical operations
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b if b != 0 else "Division by zero is not allowed"

    #Display results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
except ValueError:
    print("Invalid input. Please enter numeric values.")