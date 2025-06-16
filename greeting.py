# greeting.py
try:
    # Take input from the user
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    # Validate inputs
    if not first_name or not last_name:
        print("Error: First name and last name cannot be empty.")
    else:
        print(f"Hello, {first_name} {last_name}! Welcome to the Python course!")

except Exception as e:
    print(f"Error: An unexpected error occurred - {e}")