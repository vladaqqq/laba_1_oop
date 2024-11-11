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

class Concert(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, artist, genre_of_music):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._genre_of_music = genre_of_music
        self._artist = artist

    def find_out_the_location(self):
        if 1 <= self._seats <= 100:
            return "Your seat in the VIP zone"
        if 100 <= self._seats <= 500:
            return "Your seat in the dance floor area"
        if 500 <= self._seats <= 1000:
            return "Your seat in the balcony area"

class Cinema(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, forms, age_limit):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._forms = forms
        self._age_limit = age_limit
        self._menu_food_cinema = ['cola', 'water', 'chips', 'popcorn', 'hot_dog', 'juice', 'nachos']
        self._order_food_cinema = []

    def order_for_cinema(self, item):
        if item is self._menu_food_cinema:
            self._price += 150
            self._order_food_cinema.append(item)
            return f"Append(order='{self._order_food_cinema}', price={self._price}"
        else:
            return "This is not on the menu"

class Theatre(Event):
    def __init__(self, idd, event_name, date, location, price, tickets, seats, genre, cast):
        Event.__init__(self, idd, event_name, date, location, price, tickets, seats)
        self._genre = genre
        self._cast = cast
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
