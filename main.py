class Event:
    def __init__(self, idd, event_name, date, location, price):
        self._idd = idd
        self._event_name = event_name
        self._date = date
        self._location = location
        self._price = price

    def __repr__(self):
        return (f"Event(id={self._idd}, event_name='{self._event_name}', date={self._date}, location='{self._location}'"
                f", price={self._price}")


class SportEvent(Event):