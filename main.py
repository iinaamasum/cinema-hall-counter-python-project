""" 
 * Project: Cinema hall counter management system
 * Author: iinaamasum
 * Date: 31/10/2022
"""

""" 
    * description:
    Make a method in Hall class named view_available_seats() which will take an id of show, and view the seats that are available in that show	
"""

import re
from secrets import choice
from xml.etree.ElementInclude import default_loader


# Star_Cinema class
class Star_Cinema:
    hall_list = []

    # hall entry
    def entry_hall(self, hall):
        self.hall_list.append(hall)


# Hall class
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self, self)

    # show entry
    def entry_show(self, id, movie_name, time):
        info = (id, movie_name, time)
        self.show_list.append(info)

        for i in range(self.rows):
            self.seats[id] = []
            for j in range(self.cols):
                self.seats[id].append(["free" for i in range(self.cols)])

    # convert choice into row and col
    def convert_choice(self, choice):
        choice = choice.upper()

        # checking row
        if ord(choice[0]) - 65 > self.rows - 1:
            print("Choice is out of the capacity of the hall")
            return -1, -1
        elif "A" <= choice[0] <= "Z":
            row = ord(choice[0]) - 65
        else:
            print("Invalid seat number provided")
            return -1, -1

        # checking col
        if 0 < int(choice[1]) <= self.cols:
            col = int(choice[1]) - 1
        elif int(choice[1]) > self.cols:
            print("Choice is out of the capacity of the hall")
            return -1, -1
        else:
            print("Invalid seat number provided")
            return -1, -1
        return row, col

    # book seats
    def book_seats(self, customer_name, customer_phone_number, id):
        if not id in self.seats:
            print("Invalid show id provided")
            return
        seat_choice = input("Enter the seat number: ")
        row, col = self.convert_choice(seat_choice)

        if row == -1 or col == -1:
            return

        if self.seats[id][row][col] == "free":
            self.seats[id][row][col] = (customer_name, customer_phone_number)
            print(f"\n{seat_choice.upper()} Seat booked successfully\n")
            return
        else:
            print("\nSeat already booked\n")
            return

    # view all shows
    def view_show_list(self):
        print("-" * 80)
        print("Show list:\n")
        for i in self.show_list:
            print(f"Show ID: {i[0]}\t\tStart Time: {i[2]}\t\tShow Name: {i[1]}")
        print("-" * 80)
        print()

    # view available show seats by id
    def view_available_seats(self, id):
        if id in self.seats:
            print("=" * 80)
            print("Available seats:\n")
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[id][i][j] != "free":
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
        print("#" * 80)
        print("1) View all shows.")
        print("2) Available seats.")
        print("3) Book seats.")
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
        elif choice == 0:
            print("Good bye!")
            break
        else:
            print("Invalid choice provided")
            continue
