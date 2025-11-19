import datetime
import random
print("WELCOME TO CHATBOT WHERE YOU CAN TALK TO A SIMPLE CODE")

def chatbot():
    print("Hello! I'm your chatbot. Type 'help' to see the available commands.\n")

while True:
    inp_1 = input(">>> ").lower().strip()

    conversation = {
        "hi": "Hello there!",
        "what's your name": "My creator named me Natasha, and I'm your chatbot assistant.",
        "what's your objective": "My creator designed me to help you and make your life much more interesting.",
        "how are you": "I'm doing absolutely fantastic, thanks for asking.",
        "what do you like": "I like chatting with you especially helping and spending time with you",
        "who made you": "A young man with the name of Niko Sean Pascual.",
        "how old are you": "technically I'm only a few minutes years old...but I am more mature than most adults.",
        "what's your gender": "well since I'm only a chatbot assistant, I'm technically genderless..but for some odd reason my creator told me that my gender is female, because he said 'most chatbots have female voices so your gender is female as well.', which is quite a stereotype",
        "bye": "Goodbye, I hope I see you again so we can play games, talk and more in the future :)."
    }

    fun = {
        "tell me a joke": random.choice([
            "On what grounds did the police arrest the devil? They got him on possession.",
            "What did one fish in a tank say to the other fish in the tank? 'Do you know how to drive this thing?'",
            "What do rich people say when they tickle babies? 'Gucci, Gucci, goo.'",
            "How many therapists does it take to change a lightbulb? Only one, but the lightbulb has to want to change.",
            "Why don’t anteaters ever get sick? Their anty-bodies keep them healthy.",
            "Why do cemeteries have fences around them? Because everyone’s dying to get in.",
            "Did you hear about the guy who got the left side of his body amputated? He’s all RIGHT now",
            "My mom died when we couldn’t remember her blood type. The last thing she said was, 'Be positive.' But it’s hard without her.",
            "Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
            "My husband and I have reached the difficult decision that we do not want children. If anybody does, please just send me your contact details, and we can drop them off tomorrow.",
            "A dyslexic atheist lies awake at night wondering if there really is a dog."
        ]),
        "give me a fact": random.choice([
            "People can have a psychological disorder called Boanthropy that makes them believe that they are a cow. They try to live their life as a cow.",
            "The first roller coaster was used to transport coal down a hill. After people found that it could reach speeds up to 50 miles per hour, tourists asked to ride on it for a few cents.",
            "It took the creator of the Rubik’s Cube, Erno Rubik, one month to solve the cube after creating it; as of June 2018, the world record is 4.22 seconds.",
            "Ketchup originated in China as a boiled-down brine of pickled fish and spices called “ke-chiap.”",
            "In 2014, Sony made a cassette tape that can store 185TB of data!",
            "There is an opposite of albino animals, which aren’t white, but black. These are known as Melanistic animals.",
            "In October 2015, United Airlines made a man with Cerebral Palsy crawl off one of its flights. The flight attendants just watched as he struggled.",
            "The brain is our fattiest organ and is composed of nearly 60% fat.",
            "February used to be the last month of the year, which is why it has the shortest number of days."
        ]),
        "motivate me": random.choice([
            "Keep going — every expert was once a beginner.",
            "Believe you can and you're halfway there.",
            "You are capable of amazing things!"
        ]),
        "compliment me": random.choice([
            "You're doing great!",
            "You have a brilliant mind!",
            "Your coding skills are impressive!"
        ]),
        "i'm sad": "I'm here for you. Want to hear a joke to cheer you up?",
        "i'm happy": "That's awesome! Keep smiling!"
    }

    if inp_1.lower().strip() == "help":
        print("============ COMMANDS ============\n"
          "🗣️  Conversation:\n"
          "hi, what's your name, what's your objective, how are you, what do you like, who made you, how old are you, what's your gender, bye\n\n"
          "🕒  Utilities:\n"
          "time, date, coinflip, calculate, weather\n\n"
          "🎮  Games:\n"
          "guess the number, quiz game\n\n"
          "💬  Fun & Feelings:\n"
          "tell me a joke, give me a fact, motivate me, compliment me, I'm sad, I'm happy\n"
          "==================================\n")
    elif inp_1 == "time":
        now = datetime.datetime.now()
        print("The current time is:", now.strftime("%I:%M %p"))

    elif inp_1 == "date":
        today = datetime.date.today()
        print("Today's date is:", today.strftime("%B %d, %Y"))

    elif inp_1 == "coinflip":
        print("The coin landed on:", random.choice(["Heads", "Tails"]))

    elif inp_1 == "calculate":
        expression = input("Enter a math expression: ")
        try:
            result = eval(expression)
            print("Result:", result)
        except:
            print("Invalid expression!")

    elif inp_1 == "weather":
        print(random.choice([
            "It looks sunny today ☀️",
            "It's a bit cloudy ☁️",
            "Looks like it might rain 🌧️"
        ]))

    elif inp_1 == "guess the number":
        number = random.randint(1, 10)
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("You got it!")
        else:
            print(f"Oops, it was {number}!")

    elif inp_1 == "quiz game":
        print("Let's play! What’s the capital of Japan?")
        ans = input("→ ").lower().strip()
        if ans == "tokyo":
            print("Correct!")
        else:
            print("Nope, it's Tokyo.")

        # === CONVERSATION / FUN ===
    elif inp_1 in conversation:
        print(conversation[inp_1])
        if inp_1 == "bye":
            break

    elif inp_1 in fun:
        print(fun[inp_1])

    else:
        print("I didn’t understand that. Type 'help' to see commands.")