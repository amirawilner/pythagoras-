import random

def generate_question():
    option = random.randint(0, 2)  
    if option == 0:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = round((a**2 + b**2)**0.5, 2)  
        return a, b, c, "c"
    elif option == 1:
        a = random.randint(1, 20)
        c = random.randint(a + 1, 30)
        b = round((c**2 - a**2)**0.5, 2)  
        return a, b, c, "b"
    else:
        b = random.randint(1, 20)
        c = random.randint(b + 1, 30)
        a = round((c**2 - b**2)**0.5, 2)  
        return a, b, c, "a"

def check_answer(a, b, c, answer, option):
    if option == "c":
        expected_answer = round((a**2 + b**2)**0.5, 2)
    elif option == "b":
        expected_answer = round((c**2 - a**2)**0.5, 2)
    else:
        expected_answer = round((c**2 - b**2)**0.5, 2)
    return expected_answer, abs(answer - expected_answer) <= 0.01

def main():
  
 

    a, b, c, option = generate_question()
    if option == "c":
        print(f"\nQuestion: What is the length of the hypotenuse (c) when a = {a} and b = {b}?")
    elif option == "b":
        print(f"\nQuestion: What is the length of the missing side (b) when a = {a} and c = {c}?")
    else:
        print(f"\nQuestion: What is the length of the missing side (a) when b = {b} and c = {c}?")

    answer = float(input("Your answer: "))
    expected_answer, is_correct = check_answer(a, b, c, answer, option)

    if is_correct:
        print("Correct!")
    else:
        print(f"Wrong answer!")

    print(f"The correct answer is {expected_answer}.")

if __name__ == '__main__':
    main()