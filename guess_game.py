import random
try:
    no_of_guesses = 0
    answer = random.randint(1, 10)
    while True:
        guess = int(input("enter a number: "))
        if (guess < 1) and (guess > 10):
            print("enter a number btw 1 and 10")
        else:
            if guess == answer:
                print(f"you win! 😃✌️ the correct answer is {answer}")
                break
            else:
                no_of_guesses += 1
                print(f"Wrong Guess!! you have {3 - no_of_guesses} remaining🤕")
                if no_of_guesses == 3:
                    print(f"you lose 😔 the correct answer is {answer}")
                    break
except:
    print("what the hell did you enter??😒")


