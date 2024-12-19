#Task 1

def validate_name(name, name_type):
    if len(name) < 2:
        print(f"Error: The {name_type} name must be at least 2 characters long.")
        return False
    return True

# Main script
def main():
    # Ask for the user's first name
    first_name = input("Please enter your first name: ")
    
    # Validate the first name
    if not validate_name(first_name, "first"):
        return  # Exit if the first name is invalid
    
    # Ask for the user's last name
    last_name = input("Please enter your last name: ")
    
    # Validate the last name
    if not validate_name(last_name, "last"):
        return  # Exit if the last name is invalid
    
    # If both names are valid, print a success message
    print("Your name is valid!")

# Call the main function to execute the program
main()