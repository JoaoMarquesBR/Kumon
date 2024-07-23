import random 
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def header():
    print("Welcome to Math Practice 1.0.0\n")

def question_return(question):
    return (int)(input(question))

def highest_digits(digits):
    print("hello")

def start_multiplication(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number):
    print("\nStarting multiplication exercises\n")
    while True:
        random_number_a = random.randint(lowest_a_number,highest_a_number)
        random_number_b = random.randint(lowest_b_number,highest_b_number)

        while True : 
            response = int(input(f"{random_number_a} * {random_number_b}: "))
        
            if ( random_number_a * random_number_b) == response : 
                print(f"{GREEN}Correct response{RESET}\n")
                break
            else:
                print(f"{RED}Wrong response, please try again\n{RESET}")
            

def multiplication_setup():
    two_digits = False
    print("Numbers = A * B \n")
    lowest_a_number = (int)(input("lowest number for A:"))
    highest_a_number = (int)(input("highest number for A:"))

    print("")
    lowest_b_number = (int)(input("lowest number for B:"))
    highest_b_number = (int)(input("highest number for B:"))

    start_multiplication(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number)

def select_math_practice(value):
    print("\n")
    if value == 1:
        multiplication_setup()

def menu_selection():
    print("1 - Practice Multiplication\n")
    option_selected = (int)(input("Input Option: "))
    select_math_practice(option_selected)


header()
menu_selection()