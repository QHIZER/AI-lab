# Vacuum Cleaner Problem

# Environment: A and B
print("1WN24CS098")
rooms = {"A": "Dirty", "B": "Dirty"}

current_room = input("Enter starting room (A/B): ").upper()

while True:
    print("\nCurrent Room:", current_room)
    print("Room Status:", rooms)

    if rooms[current_room] == "Dirty":
        print("Action: Suck")
        rooms[current_room] = "Clean"
    else:
        print("Action: No Operation")

    # Check if all rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nAll rooms are clean!")
        break

    # Move to the other room
    if current_room == "A":
        print("Action: Move Right")
        current_room = "B"
    else:
        print("Action: Move Left")
        current_room = "A"