from Event import Event


class Cinema(Event):
    """Класс для представления мероприятий в кино"""
    def __init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets, forms, age_limit):
        Event.__init__(self, idd, event_name, date, location, price, free_tickets, booked_tickets)
        self._forms = forms
        self._age_limit = age_limit
        self._menu_food_cinema = ['cola', 'water', 'chips', 'popcorn', 'hot_dog', 'juice', 'nachos']
        self._order_food_cinema = []

    def order_for_cinema(self, item):
        """Метод для заказа еды в кино"""
        if item in self._menu_food_cinema:
            self._price += 150
            self._order_food_cinema.append(item)
            return f"Append(order='{self._order_food_cinema}', price={self._price}"
        else:
            return "This is not on the menu"

    def __repr__(self):
        return (f"Event(id = {self._idd}, event_name = '{self._event_name}', date = '{self._date}', "
                f"location = '{self._location}', price={self._price}, free_tickets = {self._free_tickets} , "
                f"booked_tickets = {self._booked_tickets}, forms = '{self._forms}', age_limit = {self._age_limit})")

    def get_age_limit(self):
        return self._age_limit
