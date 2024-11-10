class Event:
    def __init__(self, idd, event_name, date, location, price, tickets, seats):
        self._idd = idd
        self._event_name = event_name
        self._date = date
        self._location = location
        self._price = price
        self._tickets = tickets
        self._seats = seats

    def __repr__(self):
        return (f"Event(id={self._idd}, event_name='{self._event_name}', date={self._date}, location='{self._location}'"
                f", price={self._price}")

class SportEvent(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)


class Concert(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)

class Cinema(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)

class Theatre(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)


