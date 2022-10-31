""" 
 * Project: Cinema hall counter management system
 * Author: iinaamasum
 * Date: 31/10/2022
"""


# Star_Cinema class
class Star_Cinema:
    _hall_list = []

    # hall entry
    def entry_hall(self, hall):
        self._hall_list.append(hall)


# Hall class
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self, self)

    # show entry
    def entry_show(self, id, movie_name, time):
        info = (id, movie_name, time)
        self.__show_list.append(info)

        for i in range(self.__rows):
            self.__seats[id] = []
            for j in range(self.__cols):
                self.__seats[id].append(["free" for i in range(self.__cols)])

    # convert choice into row and col
    def convert_choice(self, choice):
        choice = choice.upper()

        # checking row
        if ord(choice[0]) - 65 > self.__rows - 1:
            print()
            print("Choice is out of the capacity of the hall")
            return -1, -1
        elif "A" <= choice[0] <= "Z":
            row = ord(choice[0]) - 65
        else:
            print()
            print("Invalid seat number provided")
            return -1, -1

        # checking col
        if 0 < int(choice[1]) <= self.__cols:
            col = int(choice[1]) - 1
        elif int(choice[1]) > self.__cols:
            print()
            print("Choice is out of the capacity of the hall")
            return -1, -1
        else:
            print()
            print("Invalid seat number provided")
            return -1, -1
        return row, col

    # book seats
    def book_seats(self, customer_name, customer_phone_number, id):
        if not id in self.__seats:
            print("Invalid show id provided")
            return
        seats_request = int(input("Enter the number of seats you want to book: "))
        seat_choice = []
        count = 1
        while seats_request > 0:
            seat_number = input(f"Enter seat choice {count}: ")
            row, col = self.convert_choice(seat_number)
            if row == -1 or col == -1:
                print("Enter seat number again")
                print()

            elif self.__seats[id][row][col] == "free":
                self.__seats[id][row][col] = (customer_name, customer_phone_number)
                seat_choice.append(seat_number.upper())
                seats_request -= 1
                count += 1
            else:
                print("\nSeat already booked\n")
                print("Enter seat number again")
                print()

        print("\nSeats booked successfully")
        print("+" * 80)
        print(
            f"Customer Name: {customer_name}\t\tCustomer Phone Number: {customer_phone_number}"
        )
        print()
        for show in self.__show_list:
            if show[0] == id:
                print(f"Show Name: {show[1]}\t\tShow Time: {show[2]}")
                break
        print("Seats:\t", end="")
        for i in seat_choice:
            print(f"{i}", end="")
            if i != seat_choice[-1]:
                print(", ", end="")
        print("\t\t\tHall No: ", self.__hall_no)
        print("+" * 80)
        print()

    # view all shows
    def view_show_list(self):
        print()
        print("-" * 80)
        print("Show list:\n")
        for i in self.__show_list:
            print(f"Show ID: {i[0]}\t\tStart Time: {i[2]}\t\tShow Name: {i[1]}")
        print("-" * 80)
        print()

    # view available show seats by id
    def view_available_seats(self, id):
        if id in self.__seats:
            print("=" * 80)
            print("Available seats:\n")
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__seats[id][i][j] != "free":
                        print("Booked\t\t", end=" ")
                    else:
                        print(f"{chr(i + 65)}{j + 1}\t\t", end=" ")
                print()
            print("=" * 80)
            print()
        else:
            print("Invalid show id provided")
            return


if __name__ == "__main__":
    hall = Hall(5, 5, "Hall123")
    hall.entry_show("Show1234", "Aj Robibar - Natok", "Oct 31, 2022 1:00PM")
    hall.entry_show("Show0011", "Aynabaji - Movie", "Oct 31, 2022 9:00PM")

    print("Welcome to Star Cinema")
    while True:
        print()
        print("#" * 80)
        print("1) View all shows.")
        print("2) Available seats.")
        print("3) Book seats.")
        print("4) Add Show.")
        print("0) Exit.")
        print("#" * 80)
        print()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            hall.view_show_list()
        elif choice == 2:
            id = input("Enter the show id: ")
            hall.view_available_seats(id)
        elif choice == 3:
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            id = input("Enter the show id: ")
            hall.book_seats(name, phone, id)
        elif choice == 4:
            show_id = input("Enter the show id: ")
            show_name = input("Enter the show name: ")
            show_time = input("Enter the show time: ")
            hall.entry_show(show_id, show_name, show_time)
            print(f"\n{show_name} added successfully")
        elif choice == 0:
            print("Good bye!")
            break
        else:
            print("Invalid choice provided")
            continue
