import random
wrong_count = -1
while True:
    try:
        no_of_guesses = 0
        answer = random.randint(1, 11)
        while True:
            guess = int(input("enter a number: "))
            if (guess < 1) or (guess > 10):
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
        wrong_count += 1
        match wrong_count:
            case 0:
                print("what the hell did you enter??😒")
            case 1:
                print("fir se galti😔")
            case 2:
                print("bhai kitni galti karega 😑")
            case 3:
                print("tu rehne de 🤚😒")
                break3


