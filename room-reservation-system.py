import random  # This one is to help us make random numbers for the booking code, like lucky draw!
 
# Global room data, all the info about the rooms we keep here
rooms = [0, 0, 0, 0]          # 0 means room empty, 1 means got people inside
codes = ["", "", "", ""]      # This one keep the secret code for each room
times = [0, 0, 0, 0]          # This one remember what time you start using the room
fee = 5                       # Every hour need to pay $5, ok lah not too expensive
admin_password = "admin123"   # This one is the secret password for the boss (admin) to see all the room status
 
def menu():
    # This function show the main menu, like when you go canteen got menu to choose food
    print("Welcome to Docking System Reservation")
    while True:  # This one means keep showing the menu until you want to exit
        print("\nMain Menu")
        print("1. Book Session")  # Option 1: Book a room
        print("2. End Session")   # Option 2: Finish using the room
        print("3. View Room Status (Admin)")  # Option 3: Only admin can see all room status
        print("4. Exit")          # Option 4: Bye bye, leave the program
 
        choice = input("Enter your choice: ")  # Ask user what they want to do
 
        if choice == '1':
            book_room()  # If choose 1, go and book room
        elif choice == '2':
            end_session()  # If choose 2, end the session
        elif choice == '3':
            view_status()  # If choose 3, see the room status (need password)
        elif choice == '4':
            print("Thank you for using our system.")  # Say thank you and stop the program
            break
        else:
            print("Invalid choice. Please try again.")  # If type wrong number, tell them try again

def book_room():
    # This function help user to book a room
    for i in range(4):  # Check all 4 rooms, see got empty or not
        if rooms[i] == 0:  # If room is empty
            while True:
                time = input("Enter start hour (0-23) for Room " + str(i+1) + ": ")  # Ask what time you want to start
                if time.isdigit() and 0 <= int(time) <= 23:  # Make sure time is correct
                    time = int(time)
                    break
                print("Invalid time. Please enter a value between 0 and 23.")  # If time wrong, ask again
            code = str(random.randint(1000, 9999))  # Generate a random 4-digit code for you, like secret password
            rooms[i] = 1  # Mark the room as booked
            codes[i] = code  # Save your code
            times[i] = time  # Save your start time
            print("Room " + str(i+1) + " booked! Your 4-digit code is: " + code)  # Tell you the room and code
            return  # After book, no need check other rooms already
    print("All rooms are currently full.")  # If all rooms got people, cannot book
 
def end_session():
    # This function help user to finish using the room
    print("Ending a Session")
    room_number = input("Enter your room number (1-4): ")  # Ask which room you use
    if not room_number.isdigit() or not (1 <= int(room_number) <= 4):  # Make sure room number is correct
        print("Invalid room number.")
        return
    room_index = int(room_number) - 1  # Change to list index (start from 0)
    if rooms[room_index] == 0:  # If room not booked, cannot end session
        print("This room is not currently booked.")
        return
 
    # Give you 3 tries to type the correct code, if not, too bad
    for attempt in range(3):
        code = input("Enter your 4-digit booking code: ")  # Ask for your secret code
        if code == codes[room_index]:  # If code correct
            exit_time = int(input("Enter exit time (0-23): "))  # Ask what time you finish
            hours = (exit_time - times[room_index]) % 24  # Calculate how many hours you use
            cost = hours * fee  # Calculate how much to pay
            print("Total time used: " + str(hours) + " hour(s)")
            print("Total fee: $" + str(cost))
            # Free the room, so next person can use
            rooms[room_index] = 0
            codes[room_index] = ""
            times[room_index] = 0
            return
        else:
            print("Wrong code. Try again.")  # If code wrong, ask again
    print("Too many failed attempts.")  # After 3 times still wrong, cannot end session
 
def view_status():
    # This function for admin to see all the room status
    print("View Room Status")
    for attempt in range(3):  # Give admin 3 tries to type password
        password = input("Enter admin password: ")
        if password == admin_password:  # If password correct
            in_use = 0
            for i in range(4):
                status = "Occupied" if rooms[i] == 1 else "Available"
                print("Room " + str(i+1) + ": " + status)
                if rooms[i] == 1:
                    in_use += 1
            print("Total rooms in use: " + str(in_use))
            print("Total rooms available: " + str(4 - in_use))
            return
        else:
            print("Wrong password.")  # If password wrong, tell admin
    # After 3 times still wrong, cannot see status
    print("Access denied.")
 
# Start the program, call the menu function to begin
menu()
