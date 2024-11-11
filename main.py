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
    def __init__(self, idd, event_name, date, location, price, tickets, seats, sector, type_of_sport):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._sector = sector
        self._type_of_sport = type_of_sport

class Concert(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, artist, genre_of_music):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._genre_of_music = genre_of_music
        self._artist = artist

class Cinema(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, forms, age_limit):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._forms = forms
        self._age_limit = age_limit

class Theatre(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, genre, cast):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._genre = genre
        self._cast = cast
