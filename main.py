# Programmed by Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: September 18, 2024
# Programming Assignment: 02

# The purpose of this code is to generate an adventure game that prompts the user and makes decisions based on it's input

# Asks user to input their name
print('Hello Challenger!, What is your name?')
user_name = input()

# Greet user and outputs story elements
print('Hello ' + user_name + '! You are in an abandoned high school with your friends and'
' notice there is a person there acting strange.')

print('One of your friends approach this strange person.')
print('They knock them down and begin biting into their flesh.')
print('Do you flee or go to save your friend?')

# Ask the user to input their first decision
first_decision = input().lower()

# Continue to ask the user to input a valid value, if they input an invalid value (Error Checking)
while first_decision not in ['flee', 'save', 'save friend', 'save my friend']:
    print('Invalid Input! Enter a valid input!')
    first_decision = input().lower()

# If user chooses to save their friend, output story elements, and ask another decision question
if first_decision == 'save my friend' or first_decision == 'save' or first_decision == 'save friend':
    print('If you go to save your friend, you must fight the stranger with the rest of your friends.')
    print('How many friends do you have to help you?')
    num_friends = int(input())

    if num_friends <= 2:
        print('Bad luck ', user_name, 'You and your friends are overwhelmed by the man')
        print('You lose!')
    if num_friends == 3:
        print('Two more of your friends become bitten by the stranger')
        print("But you're able to temporarily escape!")
        print('You and your friends lock yourselves in a classroom.')
        print('Since now three of your friends are bitten, you need to find medical supplies urgently.')
        print("You're presented with three different wards that you can go to.")

# Asks user another decision, and collects their input
        print("Do you go down the Blue ward, Red ward, or Green ward?")
        chosen_ward = input().lower()

# Continue to ask the user to input a valid value, if they input an invalid value (Error Checking)
        while chosen_ward not in ['red', 'blue', 'green']:
            print('Invalid Input! Enter a valid input!')
            chosen_ward = input().lower()

# Based on user inputs, output game status values
        if chosen_ward == 'red':
            print("Bad choice", user_name,"!")
            print("You and your friends run into a horde, and they devour your flesh!")
            print('You lose!')
        if chosen_ward == 'blue':
            print('You and your friends find medical supplies, and can escape successfully.')
            print('Congratulations ', user_name, 'You win!')
        if chosen_ward == 'green':
            print('You and your friends don’t find medical supplies and your bit friends turn into zombies')
            print('They all surround you and devour your flesh.')
            print('You lose!')
    if num_friends > 4:
        print('You and your friends trap the strange man in a locker while you and your friends escape the high school.')
        print('Congratulations ', user_name, 'You win!')

# If user chooses to flee, output story elements to the user, ask them a question, and collect their input
if first_decision == 'flee':
    print('You run until you approach three different hallways.')
    print('What hallway would you choose to go down?')
    chosen_hallway = input().lower()

# Continue to ask the user to input a valid value, if they input an invalid value (Error Checking)
    while chosen_hallway not in ['1', '2', '3']:
        print('Invalid Input! Enter a valid input!')
        chosen_hallway = input().lower()

# Based on user inputs, output story elements or end prompts to user, asks user new decision, and collects inputs
    if chosen_hallway == '1':
        print('You run down hallway number #1, you run into a horde, and meet your demise.')
        print('You lose!')
    if chosen_hallway == '2':
        print('You run down hallway #2, you run into a locked room.')
        print('You can unlock it with change in your pocket.')
        print('How much change do you have in your pocket?')
        pocket_change = float(input())

# Based on user inputs, output game status values
        if pocket_change < .25:
            print('You’re not able to open the door in time and get overwhelmed by the horde.')
            print('You lose!')
        if pocket_change > .25:
            print('You’re able to open the door in time, you call the police, and wait it out safely.')
            print('Congratulations ', user_name, 'You win!')
    if chosen_hallway == '3':
        print('You run down hallway number #3, it leads to the outside of the school and you’re free.')

