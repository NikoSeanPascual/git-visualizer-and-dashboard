import random
import time

# login success (Feel free to add more apps if you want too)
def unit_converter():
    print("=============== UNIT CONVERTER ===============\n"
          "Celsius -> Fahrenheit\n"
          "Fahrenheit -> Celsius\n"
          "Centimeters -> Inches\n"
          "Inches -> Centimeters\n"
          "Feet -> Meters\n"
          "Meters -> Feet\n")
    unit_inp = input(f"{inp} what Unit do you wanna convert? ").lower().strip()
    while True:
        unit_num_inp = input(f"{inp}, how much {unit_inp}? \n").strip()
        try:
            unit_num = float(unit_num_inp)
            break
        except ValueError:
            print("Oops! That is not a valid number. Please enter a number.")

    print("\n=============== RESULTS ===============")
    if unit_inp == "celsius":
        print(f"{str(unit_num)} Celsius: {unit_num * 1.8 + 32} Fahrenheit\n")
    elif unit_inp == "fahrenheit":
        celsius = (unit_num - 32) * 5 / 9
        print(f"{str(unit_num)} Fahrenheit: {round(celsius, 3)} Celsius\n")
    elif unit_inp == "centimeters":
        print(f"{str(unit_num)} Centimeters: {unit_num / 2.54} Inches\n")
    elif unit_inp == "inches":
        print(f"{str(unit_num)} Inches: {unit_num * 2.54} Centimeters\n")
    elif unit_inp == "feet":
        print(f"{str(unit_num)} Feet: {unit_num * 0.3048} Meters\n")
    elif unit_inp == "meter":
        print(f"{str(unit_num)} Meters: {unit_num * 3.281} Feet\n")
    else:
        print(f"it seems that your unit conversion is wrong, {unit_inp} does not exist please press (1) if you wanna try again.\n")

def letter_counter():
    print("=============== LETTER COUNTER ===============")
    text_inp = input("Put the text that you want to be checked: ").lower().strip()
    letter_inp = input("what letter do you want us to check in the text: ").lower().strip()
    print("\n=============== RESULTS ===============")
    print(f"There are {text_inp.count(letter_inp)} letter {letter_inp} in your text.\n")


def hidden_word_game():
    print("=============== HIDDEN WORD GAME ===============")
    number = random.randint(1, 10)

    for attempt in range(1, 4):
        guess = input(f"Attempt {attempt}/3 - Guess a number dear {inp} (1-10): ").strip()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == number:
            print("You got it! 🎉")
            break
        else:
            if attempt < 3:
                print("Oops! Try again.")
            else:
                print(f"Sorry, you lost. The number was {number}.")

def typing_speed_tester():
    print("=============== TYPING SPEED TEST ===============")

    type_text = [
        "Consistent practice and patience are key to mastering any skill.",
        "Writing clean and readable code is more important than writing clever code.",
        "Efficiency in programming comes from understanding algorithms deeply.",
        "Collaboration with others often leads to better software solutions.",
        "The journey of learning programming is challenging but rewarding."
    ]

    # pick 1 sentence
    sentence = random.choice(type_text)
    print(f"Type this sentence:\n{sentence}\n")

    start_time = time.time()
    user_input = input("Your answer: ")
    end_time = time.time()

    # calculate time
    time_taken = end_time - start_time

    # WPM calculation
    words = len(user_input.split())
    wpm = words / (time_taken / 60)

    # accuracy calculation
    accuracy = (1 - abs(len(sentence) - len(user_input)) / len(sentence)) * 100
    accuracy = accuracy / len(sentence) * 100

    print(f"\nTime Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

login_ok = False

while not login_ok:
    print("=============== LOG IN ===============")

    # stored account (If you want you can store multiple accounts, just use list or even dictionary)
    username = "niko sean"
    password = "12345"

    # ask name
    inp = input("What's your name? ").title().strip()

    # ask username
    inp_2 = input(f"What's your username, {inp}? ").lower().strip()

    while inp_2 != username:
        print("\nINCORRECT USERNAME, TRY AGAIN\n")
        inp_2 = input(f"What's your username, {inp}? ").lower().strip()

    # ask password
    inp_3 = input(f"What's your password, {inp}? ").lower().strip()

    while inp_3 != password:
        print("\nWRONG PASSWORD, TRY AGAIN\n")
        inp_3 = input(f"What's your password, {inp}? ").lower().strip()

    print("\nACCESS GRANTED!")
    login_ok = True
    print(f"\nWELCOME! TO MINI-OS WHERE YOU HAVE YOUR OWN MINI OPERATING SYSTEM!")
while True:
    print(f"=============== APP MENU ===============\n"
          f"1---Unit Converter\n"
          f"2---Letter Counter\n"
          f"3---Hidden Word Game\n"
          f"4---Typing Speed Tester\n"
          f"5---Exit\n")
    choice = input("Choose an app (1-4) or leave the OS (5): ").strip()

    # if you add more apps don't forget to add it here
    if choice == "1":
        unit_converter()
    elif choice == "2":
        letter_counter()
    elif choice == "3":
        hidden_word_game()
    elif choice == "4":
        typing_speed_tester()
    elif choice == "5":
        print("EXITING NIKOS-OS......")
        break
    else:
        print("Invalid Choice, Try again")