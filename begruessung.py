print("Hello World")
def how_is_the_place(message_to_print):
    how_is_the_place_variable_fuction = input(message_to_print)
    if(how_is_the_place_variable_fuction == "good"):
        return "Oh so the place is good. That's nice to hear!"
    elif (how_is_the_place_variable_fuction == "bad"):
        return "Oh so the place is bad. I'm sorry for you!"
    elif (how_is_the_place_variable_fuction == "its okay"):
        return "Oh so the place is okay. That's nice to hear!"
    else:
        return how_is_the_place("Please enter one of the valid inputs. Those are either good, bad and its okay")
def is_age_a_number(message):
    age = input()
    if(int(age)):
        return age
    else:
        return is_age_a_number("How old are you? Enter a Valid number!")
print("Hi")
name = input("Whats your name? ")
print("Hi " + name)
place = input("Where are you from?")
how_is_the_place_variable = 0

how_is_the_place_variable = how_is_the_place("Oh so you are from " + place + " how is it there? Please just say good or bad or its okay.")
print(how_is_the_place_variable)

age = is_age_a_number("How old are you?")
age += 1
print("Happy Birthday to your " + age + ". Birthday. I wish you the all the Happiness you could desire.")
print("Sorry but you ran out of Tokens. Come back tomorrow!")