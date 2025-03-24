#ACTIVITY 4.1.2 - SUBPROGRAMS
def compute_factorial(n: int) -> int: #Calculate factorial using recursion.
    if n == 0 or n == 1:
        return 1
    else:
        return n * compute_factorial(n - 1)

def check_prime(num: int) -> bool: # Check if a number is prime.
    if num <= 1:
        return False
    if num == 2:
        return True  
    if num % 2 == 0:
        return False
    for div in range(3, int(num**0.5) + 1, 2):
        if num % div == 0:
            return False
    return True

def reverse_input_string(s: str) -> str: # This will reverse a given string.
    return s[::-1]

def get_user_input(prompt: str) -> str: # This will get input from the user with the given prompt.
    return input(prompt)

def display_menu(): # This will display the main menu and handle user selections.
    while True:
        print("\n======= MENU =======")
        print("1. Calculate Factorial")
        print("2. Check Prime Numbers")
        print("3. Reverse a String")
        print("4. Exit")
        print("====================")
        
        choice = get_user_input("Please select an option (1-4): ")

        if choice == '1':
            try:
                num = int(get_user_input("Enter a non-negative integer: "))
                if num < 0:
                    print("Invalid input! Please enter a non-negative integer.")
                else:
                    print(f"The factorial of {num} is {compute_factorial(num)}.")
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '2':
            try:
                num = int(get_user_input("Enter an integer: "))
                if check_prime(num):
                    print(f"{num} is a prime number.")
                else:
                    print(f"{num} is not a prime number.")
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '3':
            s = get_user_input("Enter a string: ")
            print(f"The reversed string is: '{reverse_input_string(s)}'.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1-4).")

if __name__ == "__main__":
    display_menu()
