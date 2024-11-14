from Event import Event


class Theatre(Event):
    """Класс для представления мероприятий в театре"""
    def __init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets, genre):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets)
        self._genre = genre
        self._booklet = {
            'Romeo and Juliet': 'The duration is 2 hours. About the play: "Romeo and Juliet" is one of the most famous '
                                'and beloved tragedies by William Shakespeare, telling about the passionate love of two'
                                ' young people, Romeo and Juliet, belonging to warring families. '
                                'Their feelings become a symbol of hope for peace, but circumstances'
                                ' and prejudices lead to tragic consequences',
            'The master and Margarita': 'The duration is 3 hours. About the play: "The Master and Margarita" is a '
                                        'masterpiece by Mikhail Bulgakov, which combines elements of fiction, '
                                        'philosophy and love. The performance takes the audience into a world where '
                                        'reality and fiction meet, good and evil, as well as eternal questions about '
                                        'love and freedom',
            'The Nutcracker and the Mouse King': 'The duration is 2 hours.About the '
                                                 'play: "The Nutcracker and the Mouse '
                                                 'King" is a fairy tale written by the German writer Ernst Theodor '
                                                 'Amadeus Hoffmann in 1816. It tells about the magical adventures of a '
                                                 'girl named Clara and her toy nutcracker, who comes to life the night '
                                                 'before Christmas.'

        }

    def get_the_booklet(self, item):
        """Метод для получения буклета"""
        booklet = self._booklet.get(item)
        if booklet:
            return booklet
        else:
            return "There are no booklets for this performance"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"booked_tickets = {self._booked_tickets}, genre = '{self._genre}')")
