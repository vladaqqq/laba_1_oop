from Event import Event


class SportEvent(Event):
    def __init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets, sector):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets)
        self._sector = sector
        self._menu_food = ['cola', 'water', 'beer', 'chips', 'popcorn', 'hot_dog']
        self._order_food = []
        self._menu_souvenirs = ['trinket', 'stickers', 'cap', 'ball', 'scarf']
        self._order_souvenirs = []

    def order_food(self, item):
        if item in self._menu_food:
            self._price += 250
            self._order_food.append(item)
            return f"Append(order='{self._order_food}', price={self._price}"
        else:
            return "This is not on the menu"

    def order_souvenirs(self, item):
        if item in self._menu_souvenirs:
            self._price += 1000
            self._order_souvenirs.append(item)
            return f"Append(order='{self._order_souvenirs}', price={self._price}"
        else:
            return "This is not on the list"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"booked_tickets = {self._booked_tickets}, sector = '{self._sector}')")
