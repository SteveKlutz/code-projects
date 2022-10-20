
def displayintro():
    print("The Haunted Mansion")
    print("Collect 6 items to win the game, or die by the ghost.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'\n")


def main():
    current_room = 'Entry Room'
    # enter rooms and directions/items per room as dictionary entries
    rooms = {
        'Entry Room': {'East': 'Living Room', 'item': 'Flashlight'},
        'Living Room': {'West': 'Entry Room', 'North': 'Master Bedroom', 'South': 'Dining Room', 'East': 'Kitchen'},
        'Dining Room': {'North': 'Living Room', 'East': 'Bedroom', 'item': 'Map'},
        'Bedroom': {'West': 'Dining Room', 'item': 'SkeletonKey'},
        'Kitchen': {'North': 'Dungeon', 'West': 'Living Room', 'item': 'Batteries'},
        'Dungeon': {'South': 'Kitchen', 'item': 'Ghost!'},
        'Master Bedroom': {'South': 'Living Room', 'East': 'Master Bathroom', 'item': 'SkeletonBone'},
        'Master Bathroom': {'West': 'Master Bedroom', 'item': 'Cross'},
    }
    # declare inventory
    inventory = []
    # start while loop
    while 1:
        # print room details
        print('-----------------------------------')
        print('You are in the ' + current_room)
        print('Inventory : ' + str(inventory))
        # if current room has an item, print that you see the item
        if 'item' in rooms[current_room]:
            print('You see a ' + rooms[current_room]['item'])

        # get player move input
        player_input = input('Enter your move: ')

        # split player input for order specific command
        player_command = player_input.split()

        # if player input starts with "get"
        if player_command[0] == 'get':

            # if player input item exists in current room
            if rooms[current_room]['item'] == player_command[1]:
                inventory.append(rooms[current_room].pop('item'))

            # if item is not in current room, print invalid item
            else:
                print('Cant get ' + player_command[1] + '!')

        # if player input starts with "go"
        elif player_command[0] == 'go':
            # if player input direction exists
            if player_command[1] in rooms[current_room]:
                # current room becomes room in direction
                current_room = rooms[current_room][player_command[1]]
                if current_room == 'Dungeon':
                    # if current room is Dungeon and inventory is less than 6, you lose, end game
                    if len(inventory) < 6:
                        print('You have entered the Dungeon.')
                        print('You see a ghost!')
                        print('You do not have enough items to defend yourself.')
                        print('Game Over')
                        break
                    # if current room is Dungeon and inventory is 6 (all items), you win, end game
                    elif len(inventory) == 6:
                        print('You have entered the Dungeon.')
                        print('You see a ghost!')
                        print('You collected the necessary items to defeat the ghost!')
                        print('You win!')
                        break
            # if player command direction does not exist
            else:
                print('Invalid Direction')
        # if player command is to exit game, print Game Over and end game
        elif player_command[0] == 'exit':
            print('Game Over')
            break
        # if player command does not exist, print Invalid Entry
        else:
            print('Invalid Entry')


displayintro()
main()
