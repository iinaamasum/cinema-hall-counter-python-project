""" 
 * Project: Cinema hall counter management system
 * Author: iinaamasum
 * Date: 31/10/2022
"""

""" 
    * description:
    Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple with all of the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list, initially all seats will be free. Make a key with id to the attribute seats and value will be the 2d list.
"""

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

        print(self.seats)


h = Hall(5, 5, "ae123")
h.entry_show("ae1234", "NULL", "1:00")
