# 1.
room_list = []

# 2.
room = ["You are in the Bedrom 2. There is a passage to the north and east",1 ,3, None, None ]
room_list.append(room)
room = ["You are in the South Hall. There is a passage to the west, north and east", 0, 2, 4, None]
room_list.append(room)
room = ["You are in the Dining Room. There is a passage to the west and north", 1, 5, None, None]
room_list.append(room)
room = ["You are in the Bedroom 1. There is a passage to the east and south", 0, 4, None, None]
room_list.append(room)
room = ["You are in the North Hall. There is a passage to the west, east and south", 1, 3, 5, None]
room_list.append(room)
room = ["You are in the Kitchen. There is a passage to the west and south", 2, 4, None, None]
room_list.append(room)

# 5.
current_room = 0

# 6, 7.
print(room_list[0])