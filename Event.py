class Event:
    def __init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets):
        self._idd = idd
        self._event_name = event_name
        self._date = date
        self._location = location
        self._price = price
        self._free_tickets = free_tickets
        self._booked_tickets = booked_tickets
        self.booking_seat = list(range(booked_tickets, booked_tickets + free_tickets + 1))

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"booked_tickets = {self._booked_tickets})")

    def get_free_tickets(self):
        return self._free_tickets

    def get_booked_tickets(self):
        return self._booked_tickets

    def set_free_tickets(self, value):
        if value < 0:
            print("Error: Cannot have negative free seats.")
        else:
            self._free_tickets = value
