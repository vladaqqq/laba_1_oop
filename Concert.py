from Event import Event


class Concert(Event):
    def __init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets, artist, genre_of_music):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets)
        self._genre_of_music = genre_of_music
        self._artist = artist
        self._promo_code = ['The first purchase', 'Autumn', 'APT']
        self._key = 0

    def get_promo_code(self, item):
        if item in self._promo_code:
            if item == self._promo_code[0] and self._key == 0:
                self._key += 1
                self._price = int((self._price - self._price * 0.2))
                return "The promo code has been successfully applied"
            elif item == self._promo_code[1] and self._key == 0:
                self._key += 1
                self._price = int((self._price - self._price * 0.1))
                return "The promo code has been successfully applied"
            elif item == self._promo_code[2] and self._key == 0:
                self._key += 1
                self._price = int((self._price - self._price * 0.15))
                return "The promo code has been successfully applied"
            else:
                return "The promo code has already been applied to this ticket"
        else:
            return "The promo code is not suitable"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"booked_tickets = {self._booked_tickets}, genre_of_music = '{self._genre_of_music}', "
                f"artist = '{self._artist}')")
