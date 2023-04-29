import random, os
from time import sleep

outcome = {1:"", 2:"", 3:"", 4:""}

def results(result, outcome, round):
    if result == True:
        outcome[round] = "Win!"
        print(outcome[round])
        print("Round: " + str(outcome))
    else:
        outcome[round] = "Loss!"
        print(outcome[round])
        print("Round: " + str(outcome))


def populate(length, variance):
    list = []
    for x in range(length):
        rn = random.randint(1, variance)
        if rn == 1 or rn == 5:
            insert = 'x'
        elif rn == 2 or rn == 6:
            insert = '+'
        elif rn == 3 or rn == 7:
            insert = '='
        elif rn == 4 or rn == 8:
            insert = '&'
        list.append(insert)
    return list


def counter(list):
    counterX, counterP, counterE, counterA = 0, 0, 0, 0
    for n in list:
        if n == 'x':
            counterX += 1
        elif n == '+':
            counterP += 1
        elif n == '=':
            counterE += 1
        elif n == '&':
            counterA += 1
        else:
            print("error")
    return (counterX, counterP, counterE, counterA)


def game(list, tuple, time):

    print("The challenge will occur in...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print(list)
    sleep(time)
    print("\n" * 100)
    print("Times up!")
    sleep(1)

    rn = random.randint(1, 8)
    match rn:
        case 1:
            answer = input("Enter the amount of times the most used symbol appeared: ")
            if int(answer) == max(tuple):
                return True
            else:
                return False
        case 2:
            answer = input("Enter how many times x appeared: ")
            if int(answer) == tuple[0]:
                return True
            else:
                return False
        case 3:
            answer = input("Enter how many times + appeared: ")
            if int(answer) == tuple[1]:
                return True
            else:
                return False
        case 4:
            answer = input("Enter how many times = appeared: ")
            if int(answer) == tuple[2]:
                return True
            else:
                return False
        case 5:
            answer = input("Enter how many times & appeared: ")
            if int(answer) == tuple[3]:
                return True
            else:
                return False
        case 6:
            answer = input("Enter the symbol that appeared the most: ")
            if (answer == 'x' and tuple[0] == max(tuple) or
                answer == '+' and tuple[1] == max(tuple) or
                answer == '=' and tuple[2] == max(tuple) or
                answer == '&' and tuple[3] == max(tuple)):
                return True
            else:
                return False
        case 7:
            answer = input("Enter the symbol that appeared the least (or did not occur): ")
            if (answer == 'x' and tuple[0] == min(tuple) or
                answer == '+' and tuple[1] == min(tuple) or
                answer == '=' and tuple[2] == min(tuple) or
                answer == '&' and tuple[3] == min(tuple)):
                return True
            else:
                return False
        case 8:
            rn2 = random.randint(1, len(list))
            answer = input("Enter what symbol occured at position " + str(rn2) + ": ")
            if answer == list[rn2-1]:
                return True
            else:
                return False


# Introduction
print("You have entered a skill tournament to test both your memorization speed\n"
      "and ability in one of the highest accredited tournament institutions\n"
      "in the country.\n\nYou are able to choose which path you want to take: \n"
      "The Reaction Path, which focuses mainly on testing your ability to memorize "
      "things quickly,\nor The Matrix Path, which requires you to memorize "
      "longer patterns,\nbut in a longer period of given time.\n")

# Choose path
while True:
    path = input("Enter either Reaction or Matrix to choose your path: ")
    if path.upper() == "REACTION":
        choice = 1
        break
    elif path.upper() == "MATRIX":
        choice = 2
        break
    else:
        print("Incorrect input.")


# Start path 1
if choice == 1:
    print("You have chosen The Reaction Path.\nYour first challenge is of difficulty 1.\n"
          "It will be a starter challenge to get used to these challenges.")
    sleep(4)
    list = populate(5, 4)
    tuple = counter(list)
    result = game(list, tuple, 3)
    results(result, outcome, 1)

    print("\nYour second challenge is of difficulty 2. It will be very short,\n"
          "but will be faster, and have less variance between symbols.")
    sleep(4)
    list = populate(7, 2)
    tuple = counter(list)
    result = game(list, tuple, 2)
    results(result, outcome, 2)

    print("\nYour third challenge is of difficulty 3. It will be be similar to\n"
          "the last test, but have more variance and will be slightly "
          "longer in both length and speed.")
    sleep(4)
    list = populate(6, 3)
    tuple = counter(list)
    result = game(list, tuple, 4)
    results(result, outcome, 3)

    print("\nYour fourth challenge and final challenge is of difficulty 6.\n"
          "It is the last challenge, and thus will be\n"
          "nearly twice as difficult as the previous one.")
    sleep(4)
    list = populate(9, 4)
    tuple = counter(list)
    result = game(list, tuple, 4)
    results(result, outcome, 4)


# Start path 2
if choice == 2:
    print("\nYou have chosen The Matrix Path.\nYour first challenge is of difficulty 1.\n"
          "It will be a starter challenge to get used to these challenges.")
    sleep(4)
    list = populate(7, 2)
    tuple = counter(list)
    result = game(list, tuple, 8)
    results(result, outcome, 1)

    print("\nYour second challenge is of difficulty 2. It will be the game speed\n"
          "and length of the previous challenge, however it will\n"
          "have more variance and will be longer.")
    sleep(4)
    list = populate(9, 3)
    tuple = counter(list)
    result = game(list, tuple, 8)
    results(result, outcome, 2)

    print("\nYour third challenge is of difficulty 3. It will have more variance,\n"
          "will be slower, but will be longer.")
    sleep(4)
    list = populate(12, 6)
    tuple = counter(list)
    result = game(list, tuple, 10)
    results(result, outcome, 3)

    print("\nYour fourth and final challenge is of difficulty 6. It is the last\n"
          "challenge, and thus will be nearly twice as difficult as the previous one.")
    sleep(4)
    list = populate(16, 4)
    tuple = counter(list)
    result = game(list, tuple, 15)
    results(result, outcome, 4)


# Count score
vic = 0
for x in outcome:
    if outcome[x] == "Win!":
        vic += 1
    else:
        vic += -1

# Ending depending on score results
if vic < 0:
    print("\nYou feel an overwhelming sense of shame and frustration.\n"
          "Your loss seemed nearly inevitable, but now that\n"
          "it has finally come to fruition, the resulting emotions are unbeareable")
elif vic == 0:
    print("\nYou come to realize that you have a neuteral score.\n"
          "You feel no sense of accomplishment, but at the same time,\n"
          "you feel no shame in the loss you nearly suffered.")
else:
    print("\nYou feel a great sense of accomplishment having beat the challenges "
          "that you faced. ")

# Additional ending information based on score results and path chosen
if path == 1 and vic < 0:
    print("\nYou failed The Reaction Path.")
elif path == 1 and vic == 0:
    print("\nYou neither failed nor succeeded in beating The Reaction Path.\n"
          "Or maybe you both failed, and succeeded?")
elif path == 1 and vic > 0:
    print("\nYou beat The Reaction Path!")
elif path == 2 and vic < 0:
    print("\nYou failed The Matrix Path.")
elif path == 2 and vic == 0:
    print("\nYou neither failed nor succeeded in beating The Matrix Path.\n"
          "Or maybe you both failed, and succeeded?")
elif path == 2 and vic > 0:
    print("\nYou beat The Matrix Path!")
