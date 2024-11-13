from SportEvent import SportEvent
from Cinema import Cinema
from Concert import Concert
from Theatre import Theatre
import json
import xml.etree.ElementTree as ET


class Booking:
    booking_id_counter = 0

    def __init__(self):
        self._bookings = []

    def create(self, person, event, booking_seat_num):

        if isinstance(event, SportEvent):
            if event.get_booked_tickets() < booking_seat_num <= len(event.booking_seat):
                if booking_seat_num in event.booking_seat:
                    event.booking_seat.remove(booking_seat_num)
                    Booking.booking_id_counter += 1
                    booking_ver = {
                        'booking_id': Booking.booking_id_counter,
                        'person': person,
                        'event': event,
                        'Your seat': booking_seat_num
                    }
                    bok = event.get_free_tickets() - 1
                    event.set_free_tickets(bok)
                    self._bookings.append(booking_ver)
                else:
                    while True:
                        try:
                            booking_seat_num = int(input("Sorry this seat is "
                                                         "already booked.Please, choose another one: "))
                            Booking.create(self, person, event, booking_seat_num)
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")

                return f"The reservation has been successfully completed, " \
                       f"here is your unique id: {Booking.booking_id_counter}"
            else:
                while True:
                    try:
                        booking_seat_num = int(input("Sorry this seat is "
                                                     "already booked.Please, choose another one: "))
                        Booking.create(self, person, event, booking_seat_num)
                        break
                    except ValueError:
                        print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Cinema):
            if person.get_age() < event.get_age_limit():
                return "Sorry, u cant book ticket for this event"
            if event.get_booked_tickets() < booking_seat_num <= (event.get_free_tickets()
                                                                 + event.get_booked_tickets()):
                if booking_seat_num in event.booking_seat:
                    event.booking_seat.remove(booking_seat_num)
                    Booking.booking_id_counter += 1
                    booking_ver = {
                        'booking_id': Booking.booking_id_counter,
                        'person': person,
                        'event': event,
                        'your seat': booking_seat_num
                    }
                    bok = event.get_free_tickets() - 1
                    event.set_free_tickets(bok)
                    self._bookings.append(booking_ver)
                    return (f"The reservation has been successfully completed, here is "
                            f"your unique id: {Booking.booking_id_counter}")
                else:
                    while True:
                        try:
                            booking_seat_num = int(input("Sorry this seat is "
                                                         "already booked.Please, choose another one: "))
                            Booking.create(self, person, event, booking_seat_num)
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")

                return f"The reservation has been successfully completed, " \
                       f"here is your unique id: {Booking.booking_id_counter}"
            else:
                while True:
                    try:
                        booking_seat_num = int(input("Sorry this seat is already booked."
                                                     "Please, choose another one: "))
                        Booking.create(self, person, event, booking_seat_num)
                        break
                    except ValueError:
                        print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Concert):

            if event.get_booked_tickets() < booking_seat_num <= (event.get_free_tickets()
                                                                 + event.get_booked_tickets()):
                if booking_seat_num in event.booking_seat:
                    event.booking_seat.remove(booking_seat_num)
                    Booking.booking_id_counter += 1
                    booking_ver = {
                        'booking_id': Booking.booking_id_counter,
                        'person': person,
                        'event': event,
                        'your seat': booking_seat_num
                    }
                    bok = event.get_free_tickets() - 1
                    event.set_free_tickets(bok)
                    self._bookings.append(booking_ver)
                    return (f"The reservation has been successfully completed, here "
                            f"is your unique id: {Booking.booking_id_counter}")
                else:
                    while True:
                        try:
                            booking_seat_num = int(input("Sorry this seat is already booked."
                                                         "Please, choose another one: "))
                            Booking.create(self, person, event, booking_seat_num)
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")
            else:
                while True:
                    try:
                        booking_seat_num = int(input("Sorry this seat is already booked."
                                                     "Please, choose another one: "))
                        Booking.create(self, person, event, booking_seat_num)
                        break
                    except ValueError:
                        print("Sorry this seat is already booked.Please, choose another one: ")
        elif isinstance(event, Theatre):

            if event.get_booked_tickets() < booking_seat_num <= (event.get_free_tickets()
                                                                 + event.get_booked_tickets()):
                if booking_seat_num in event.booking_seat:
                    event.booking_seat.remove(booking_seat_num)
                    Booking.booking_id_counter += 1
                    booking_ver = {
                        'booking_id': Booking.booking_id_counter,
                        'person': person,
                        'event': event,
                        'your seat': booking_seat_num
                    }
                    bok = event.get_free_tickets() - 1
                    event.set_free_tickets(bok)
                    self._bookings.append(booking_ver)
                    return (f"The reservation has been successfully completed, here is your "
                            f"unique id: {Booking.booking_id_counter}")
                else:
                    while True:
                        try:
                            booking_seat_num = int(input("Sorry this seat is already booked."
                                                         "Please, choose another one: "))
                            Booking.create(self, person, event, booking_seat_num)
                            break
                        except ValueError:
                            print("Sorry this seat is already booked.Please, choose another one: ")
            else:
                while True:
                    try:
                        booking_seat_num = (input("Sorry this seat is already booked.Please, choose another one: "))
                        Booking.create(self, person, event, booking_seat_num)
                        break
                    except ValueError:
                        print("Sorry this seat is already booked.Please, choose another one:")

    def read_all(self):
        return self._bookings

    def read_by_id(self, booking_id):
        for boo in self._bookings:
            if boo['booking_id'] == booking_id:
                return boo
        return "No booking found with this ID"

    def update(self, booking_id, new_seat):
        for boo in self._bookings:
            if boo['booking_id'] == booking_id:
                event = boo['event']
                if new_seat in event.booking_seat:
                    old_seat = boo['Your seat']
                    event.booking_seat.append(old_seat)
                    boo['Your seat'] = new_seat
                    event.booking_seat.remove(new_seat)
                    return f"Your ticket with ID {booking_id} is successfully {new_seat}."
                else:
                    return "The new location is unavailable or already occupied."

        return "No booking with this ID was found."

    def delete(self, bok_id):
        bok = self.read_by_id(bok_id)
        if bok:
            self._bookings.remove(bok)
            return f"Person with id {bok_id} has been deleted."
        return "Person not found."

    def to_json(self, filename="bookings.json"):
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(self._bookings, json_file, default=lambda o: o.__dict__, indent=4)
        return f"Data has been saved to {filename}"

    def to_xml(self, filename="bookings.xml"):
        root = ET.Element("bookings")
        for boo in self._bookings:
            booking_element = ET.SubElement(root, "booking")

            for key, value in boo.items():
                if hasattr(value, '__dict__'):
                    value = value.__repr__()

                element = ET.SubElement(booking_element, key)
                element.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return f"Data has been saved to {filename}"
