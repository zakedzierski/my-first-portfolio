start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and you die from sepsis hahahaha") # finished the story by writing what happens

elif user_input == "right":
    print("You choose to go right and are greeted by a dinosaur. Do you approach it or do you run back?")
if user_input == "approach":
    print("You chose wisely. This dino is a friend.")
elif user_input == "run":
    print("You decide to go left and you die from sepsis hahahaha")
