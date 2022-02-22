# 1, 5, 10.
# variables
room_list = []
current_room = 0
done = False

# 2, 3, 4.
# adding rooms to list
room = ["You are in the Bedrom 2.\nThere is a passage to the north and east",3 ,1 , None, None ]
room_list.append(room)
room = ["You are in the South Hall.\nThere is a passage to the west, north and east", 4, 2, None, 0]
room_list.append(room)
room = ["You are in the Dining Room.\nThere is a passage to the west and north", 5, None, None, 1]
room_list.append(room)
room = ["You are in the Bedroom 1.\nThere is a passage to the east and south", None, 4, 0, None]
room_list.append(room)
room = ["You are in the North Hall.\nThere is a passage to the west, east, south and north", 6, 5, 1, 3]
room_list.append(room)
room = ["You are in the Kitchen.\nThere is a passage to the west and south", None, None, 2, 1]
room_list.append(room)
room = ["You are at the Balcony.\nThere is a passage to the south", None, None, 4, None]
room_list.append(room)

# 6, 7.
#print(room_list[0])

# 10.
# while loop to repeat and keep the game running
while not done:
    # 11.
    print()

    # 8, 9.
    # tells the user the current room
    print (room_list[current_room][0])
    print()

    # 12.
    # user input
    user_choice = input("Which direction? ")

    # 21.
    # quit command
    if user_choice.upper() == 'QUIT' or user_choice.upper() == 'Q':
        print()
        print("You quit the game.")
        done = True    
    
    # 13.
    # input options 
    # NORTH
    elif user_choice.upper() == 'NORTH' or user_choice.upper() == 'N' :
        # 14.
        next_room = room_list[current_room][1]
    
    # 15.
        if next_room == None:
            print()
            print("\033[31m" + "You can't go that way")
            print("\033[0m")
        else:
            current_room = next_room

    # 17.
    # EAST
    elif user_choice.upper() == 'EAST' or user_choice.upper() == 'E':
        next_room = room_list[current_room][2]

        if next_room == None:
            print()
            print("\033[31m" + "You can't go that way")
            print("\033[0m")
        else:
            current_room = next_room
    
    # SOUTH
    elif user_choice.upper() == 'SOUTH' or user_choice.upper() == 'S':
        next_room = room_list[current_room][3]

        if next_room == None:
            print()
            print("\033[31m" + "You can't go that way")
            print("\033[0m")
        else:
            current_room = next_room

    # WEST
    elif user_choice.upper() == 'WEST' or user_choice.upper() == 'W':
        next_room = room_list[current_room][4]

        if next_room == None:
            print()
            print("\033[31m" + "You can't go that way")
            print("\033[0m")
        else:
            current_room = next_room
    
    # QUIT
    else: 
        print("Invalid Input! Please try again.")