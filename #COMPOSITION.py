#COMPOSITION
class Room:
    def __init__(self, name: str):
        self.name = name

class House:
    def __init__(self):
        # The House creates and owns these Room objects directly
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

# --- Running the code ---
# 1. Instantiate the parent object (House)
my_house = House()

# 2. Iterate through the tightly coupled child objects (Rooms) created inside it
for room in my_house.rooms:
    print(f"Room created: {room.name}")

# If the House object is deleted, self.rooms is also deleted from memory
