import random 
import readJson

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def header():
    print("Welcome to Math Practice 1.0.0\n")

def question_return(question):
    return (int)(input(question))

def start_multiplication(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number,nExercises):
    print("\nStarting multiplication exercises\n")
    i = 0;
    
    while True:
        random_number_a = random.randint(lowest_a_number,highest_a_number)
        random_number_b = random.randint(lowest_b_number,highest_b_number)
        i+=1
        if(i > nExercises):
            break;
        while True : 
            response = int(input(f"#{i}: {random_number_a} * {random_number_b}: "))
        
            if ( random_number_a * random_number_b) == response : 
                print(f"{GREEN}Correct response{RESET}\n")
                break
            else:
                print(f"{RED}Wrong response, please try again\n{RESET}")
            

def exercisesNumber():
    return (int)(input("\nNumbers of exercises:"))

def multiplication_setup():
    two_digits = False
    print("Numbers = A * B \n")
    lowest_a_number = (int)(input("lowest number for A:"))
    highest_a_number = (int)(input("highest number for A:"))

    print("")
    lowest_b_number = (int)(input("lowest number for B:"))
    highest_b_number = (int)(input("highest number for B:"))

    nExercises = exercisesNumber()

    start_multiplication(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number,nExercises)

def multiplication_exam_setup(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number,nExercises):
    start_multiplication(lowest_a_number,highest_a_number,lowest_b_number,highest_b_number,nExercises)


def select_math_practice(value):
    print("\n")
    if value == 1:
        multiplication_setup()
    if value==2 :
        ec = readJson.readExamLevel("A1")
        multiplication_exam_setup(ec['min_a'],ec['max_a'],ec['min_b'],ec['max_b'],ec['nExercises'])

def menu_selection():
    print("1 - Practice Multiplication")
    print("2 - Multiplication Exam\n")

    option_selected = (int)(input("Input Option: "))
    select_math_practice(option_selected)


header()
menu_selection()