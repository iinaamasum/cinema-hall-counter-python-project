""" 
 * Project: Cinema hall counter management system
 * Author: iinaamasum
 * Date: 31/10/2022
"""

""" 
    * description:
    Make a method in Hall class named book_seats() which will take the customer name, phone number, an id of the show and list of tuples where every tuple contains the row and col of the seat. You need to check the id of the show, and book the seats. 	
"""

# Star_Cinema class
from lib2to3.pytree import convert


class Star_Cinema:
    hall_list = []

    # hall entry
    def entry_hall(self, hall):
        self.hall_list.append(hall)


# Hall class
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = [()]
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
        print(choice)

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
            print(self.seats)
            print("Seat booked successfully")
            return
        else:
            print("Seat already booked")
            return


h = Hall(5, 5, "ae123")
h.entry_show("ae1234", "NULL", "1:00")
h.book_seats("iinaamasum", "123456789", "ae1234")
