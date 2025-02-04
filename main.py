import random 
import readJson
import time

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
    i = 0;
    startTime = time.time()
    
    while True:
        random_number_a = random.randint(lowest_a_number,highest_a_number)
        random_number_b = random.randint(lowest_b_number,highest_b_number)
        i+=1
        if(i > nExercises):
            endTime = time.time()
            print(f"Duration = {(endTime-startTime)}")
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


def chooseStringFromList(list):
    i =0;
    for obj in list:
        i+=1
        print(f"{i} - {obj}")
    chosen_option = (int)(input("Chose ID: "))-1
    return list[chosen_option]

def select_math_practice(value):
    print("\n")
    if value == 1:
        multiplication_setup()
    if value==2 :
        multiplication_exam_options = readJson.readMultiplicationExamOptions()
        chosen_exam_level = chooseStringFromList(multiplication_exam_options)
        ec = readJson.readExamLevel(chosen_exam_level)
        print(f"\nStarting Multiplication Exam Level {chosen_exam_level}")
        multiplication_exam_setup(ec['min_a'],ec['max_a'],ec['min_b'],ec['max_b'],ec['nExercises'])

def menu_selection():
    print("1 - Practice Multiplication")
    print("2 - Multiplication Exam\n")

    option_selected = (int)(input("Input Option: "))
    select_math_practice(option_selected)


header()
menu_selection()