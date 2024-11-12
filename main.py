class Person:
    def __init__(self, name, age, mail, phone_number):
        self._name = name
        self._age = age
        self._mail = mail
        self._phone_number = phone_number

    def __repr__(self):
        return (f"Person(id = '{self._name}', age = {self._age}, mail = '{self._mail}', "
                f"phone_number = {self._phone_number})")

    def get_age(self):
        return self._age


class Event:
    def __init__(self, idd, event_name, date, location, price, free_tickets):
        self._idd = idd
        self._event_name = event_name
        self._date = date
        self._location = location
        self._price = price
        self._free_tickets = free_tickets
        self._free_seats = free_tickets

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"free_seats = {self._free_seats})")

    def get_free_tickets(self):
        return self._free_tickets

    def set_free_tickets(self, value):
        if value < 0:
            print("Error: Cannot have negative free seats.")
        else:
            self._free_seats = value

class SportEvent(Event):
    def __init__(self, idd, event_name, date, location, price, free_tickets, sector):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets)
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
                f"free_seats = {self._free_seats}, sector = '{self._sector}')")

class Concert(Event):
    def __init__(self, idd, event_name, date, location, price, free_tickets, artist, genre_of_music):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets)
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
                f"free_seats = {self._free_seats}, genre_of_music = '{self._genre_of_music}', "
                f"artist = '{self._artist}')")

class Cinema(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, forms, age_limit):
        Event.__init__(self, idd, event_name, date, location, price, tickets)
        self._forms = forms
        self._age_limit = age_limit
        self._menu_food_cinema = ['cola', 'water', 'chips', 'popcorn', 'hot_dog', 'juice', 'nachos']
        self._order_food_cinema = []

    def order_for_cinema(self, item):
        if item in self._menu_food_cinema:
            self._price += 150
            self._order_food_cinema.append(item)
            return f"Append(order='{self._order_food_cinema}', price={self._price}"
        else:
            return "This is not on the menu"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"free_seats = {self._free_seats}, forms = '{self._forms}', age_limit = {self._age_limit})")

    def get_age_limit(self):
        return self._age_limit

class Theatre(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, genre):
        Event.__init__(self, idd, event_name, date, location, price, tickets)
        self._genre = genre
        self._booklet = {
            'Romeo and Juliet': 'The duration is 2 hours. About the play: "Romeo and Juliet" is one of the most famous '
                                'and beloved tragedies by William Shakespeare, telling about the passionate love of two'
                                ' young people, Romeo and Juliet, belonging to warring families. Their feelings become a'
                                'symbol of hope for peace, but circumstances and prejudices lead to tragic consequences',
            'The master and Margarita': 'The duration is 3 hours. About the play: "The Master and Margarita" is a '
                                        'masterpiece by Mikhail Bulgakov, which combines elements of fiction, '
                                        'philosophy and love. The performance takes the audience into a world where '
                                        'reality and fiction meet, good and evil, as well as eternal questions about '
                                        'love and freedom',
            'The Nutcracker and the Mouse King': 'The duration is 2 hours.About the play: "The Nutcracker and the Mouse '
                                                 'King" is a fairy tale written by the German writer Ernst Theodor '
                                                 'Amadeus Hoffmann in 1816. It tells about the magical adventures of a '
                                                 'girl named Clara and her toy nutcracker, who comes to life the night '
                                                 'before Christmas.'

        }

    def get_the_booklet(self, item):
        booklet = self._booklet.get(item)
        if booklet:
            return booklet
        else:
            return "There are no booklets for this performance"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"free_seats = {self._free_seats}, genre = '{self._genre}')")


class Booking:
    def __init__(self, event):
        self._bookings = []
        self._booking_id_counter = 1
        self._booking_seat = list(range(1, event.get_free_tickets() + 1))

    def create(self, person, event, booking_seat_num):
        if isinstance(event, SportEvent):
            while True:
                if 50 < booking_seat_num <= len(self._booking_seat):
                    if booking_seat_num in self._booking_seat:
                        self._booking_seat.remove(booking_seat_num)
                        booking_id = self._booking_id_counter
                        booking_ver = {
                            'booking_id': booking_id,
                            'person': person,
                            'event': event,
                            'Your seat': booking_seat_num
                        }
                        bok = event.get_free_tickets() - 1
                        event.set_free_tickets(bok)
                        self._bookings.append(booking_ver)
                        self._booking_id_counter += 1
                        return f"The reservation has been successfully completed, here is your unique id: {booking_id}"
                else:
                    while True:
                        try:
                            booking_seat_num = int(
                                input("Sorry this seat is already booked.Please, choose another one: "))
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Cinema):
            if person.get_age() < event.get_age_limit():
                return "Sorry, u cant book ticket for this event"
            while True:
                if 20 < booking_seat_num <= len(self._booking_seat):
                    if booking_seat_num in self._booking_seat:
                        self._booking_seat.remove(booking_seat_num)
                        booking_id = self._booking_id_counter
                        booking_ver = {
                            'booking_id': booking_id,
                            'person': person,
                            'event': event,
                            'your seat': booking_seat_num
                        }
                        bok = event.get_free_tickets() - 1
                        event.set_free_tickets(bok)
                        self._bookings.append(booking_ver)
                        self._booking_id_counter += 1
                        return f"The reservation has been successfully completed, here is your unique id: {booking_id}"
                else:
                    while True:
                        try:
                            booking_seat_num = int(
                                input("Sorry this seat is already booked.Please, choose another one: "))
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Concert):
            while True:
                if 200 < booking_seat_num <= len(self._booking_seat):
                    if booking_seat_num in self._booking_seat:
                        self._booking_seat.remove(booking_seat_num)
                        booking_id = self._booking_id_counter
                        booking_ver = {
                            'booking_id': booking_id,
                            'person': person,
                            'event': event,
                            'your seat': booking_seat_num
                        }
                        bok = event.get_free_tickets() - 1
                        event.set_free_tickets(bok)
                        self._bookings.append(booking_ver)
                        self._booking_id_counter += 1
                        return f"The reservation has been successfully completed, here is your unique id: {booking_id}"
                else:
                    while True:
                        try:
                            booking_seat_num = int(
                                input("Sorry this seat is already booked.Please, choose another one: "))
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Theatre):
            while True:
                if 200 < booking_seat_num <= len(self._booking_seat):
                    if booking_seat_num in self._booking_seat:
                        self._booking_seat.remove(booking_seat_num)
                        booking_id = self._booking_id_counter
                        booking_ver = {
                            'booking_id': booking_id,
                            'person': person,
                            'event': event,
                            'your seat': booking_seat_num
                        }
                        bok = event.get_free_tickets() - 1
                        event.set_free_tickets(bok)
                        self._bookings.append(booking_ver)
                        self._booking_id_counter += 1
                        return f"The reservation has been successfully completed, here is your unique id: {booking_id}"
                else:
                    while True:
                        try:
                            booking_seat_num = int(
                                input("Sorry this seat is already booked.Please, choose another one: "))
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")

    def read_all(self):
        return self._bookings

    # def update(self):

event_1 = SportEvent(1, "Football match", "2024.12.01", "Stadium A", 500,
                     200, "Sector A")
print(event_1)
print(event_1.order_food('cola'))
print(event_1.order_souvenirs('cap'))
print(event_1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
event_2 = Concert(2, "Rock Concert", "2024.12.05", "Arena B", 800, 300,
                  "Rock Band", "Rock")
print(event_2)
print(event_2.get_promo_code('Autumn'))
print(event_2)
print(event_2.get_promo_code('APT'))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
event_3 = Cinema(3, "Going to the cinema", "2024.11.12", "CARO", 450, 10,
                 "2D", 16)
print(event_3)
print(event_3.order_for_cinema('chips'))
print(event_3.order_for_cinema('beer'))
print(event_3)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
event_4 = Theatre(3, "Romeo and Juliet", "2025.12.10", "The Big theatre", 7500,
                  200, 'tragedy')
print(event_4)
print(event_4.get_the_booklet('Romeo and Juliet'))

person_1 = Person("Alice", 25, "alice@example.com", "1234567890")

booking = Booking(event_1)
print(booking.create(person_1, event_1, 129))
print(booking.read_all())
