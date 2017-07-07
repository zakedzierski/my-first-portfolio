start = '''
You wake up one morning on top of a hill.
Choose a direction to walk in.
Type 'north' to go north, 'west' to go west, 'east' to go east, or 'south' to go south.
'''

print(start)

user_input = input()
if user_input == "north" or user_input == "west":
  print("You are dead! You fell down the hill trying to run too fast and broke all your bones.") # finished the story by writing what happens

if user_input == "east":
    print("You encounter a house. Do you enter it? Type 'yes' to enter or type 'no' to burn it down.")
    user_input = input()
    if user_input == "no":
        print("You are arrested by the police for arson and you die in prison an hour later.") # finished the story by writing what happen
    elif user_input == "yes":
        print("You see a HUGE bottle of something that looks like beer. Type 'drink' to drink it or 'no' to see what happens.")

        user_input = input()
        if user_input == "drink":
            print("You just died from alcohol poisoning. Sucks to suck.") # finished the story by writing what happens
        elif user_input == "no":
            print("You move into the house and live there happily ever after.") # finished the story by writing what happens

elif user_input == "south":
    print("You run into a dinosaur. Do you run back west or approach and talk to it? Type 'run' to run back or type 'talk' to approach the dino.")

    user_input = input()
    if user_input == "run":
        print("Die. You judged the dino too harshly and he got angry. So, he shoots you as you run.") # finished the story by writing what happens
    elif user_input == "talk":
        print("You have a kind and brave heart! The dino repays your kindness and gives you a house and a dog. You win, ALWAYS BE NICE!") # finished the story by writing what happens
