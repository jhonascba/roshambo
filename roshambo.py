from random import randrange


def play():
    print("********** RO-SHAM-BO **********")

    values = ["ROCK", "PAPER", "SCISSORS"]

    name = str(input("Type your name: ")).strip()

    won = False
    lost = False
    computer_score = 0
    user_score = 0

    while not won and not lost:

        number = randrange(0, len(values))
        computer_choice = values[number]

        print(f"{name} {user_score} X {computer_score} Computer")
        print("[ 0 ] ROCK")
        print("[ 1 ] PAPER")
        print("[ 2 ] SCISSORS")

        user_choice = None

        try:
            value_choose = int(input("Type your choice: "))
        except ValueError:
            print("Invalid value!")
            continue

        if value_choose not in range(0, 3):
            print("Invalid value!\n")

        else:
            for _ in values:
                user_choice = values[value_choose]

            if value_choose == number:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print("Draw!\n")

            elif value_choose == 0 and number == 1:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print("Computer scored!\n")
                computer_score += 1

            elif value_choose == 0 and number == 2:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print(f"{name} scored!")
                user_score += 1

            elif value_choose == 1 and number == 0:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print(f"{name} scored!")
                user_score += 1

            elif value_choose == 1 and number == 2:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print("Computer scored!\n")
                computer_score += 1

            elif value_choose == 2 and number == 0:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print("Computer scored!\n")
                computer_score += 1

            elif value_choose == 2 and number == 1:
                print(f"Computer chose {computer_choice}")
                print(f"{name} chose {user_choice}")
                print(f"{name} scored!")
                user_score += 1

        won = user_score == 10
        lost = computer_score == 10

    if won:
        print("You won!")
        print("Final score:")
        print(f"{name} {user_score} X {computer_score} Computer")
    else:
        print("You lost!")
        print("Final score:")
        print(f"{name} {user_score} X {computer_score} Computer")


if __name__ == "__main__":
    play()
