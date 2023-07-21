import random

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = round((a**2 + b**2)**0.5, 2)  
    return a, b, c, "c"

def check_answer(a, b, c, answer, option):
    expected_answer = round((a**2 + b**2)**0.5, 2)
    return expected_answer, abs(answer - expected_answer) <= 0.01

def main():
   
 

    a, b, c, option = generate_question()
    print(f"\nQuestion: What is the length of the hypotenuse (c) when a = {a} and b = {b}?")

    answer = float(input("Your answer: "))
    expected_answer, is_correct = check_answer(a, b, c, answer, option)

    if is_correct:
        print("Correct!")
    else:
        print(f"Wrong answer!")

    print(f"The correct answer is {expected_answer}.")

if __name__ == '__main__':
    main()