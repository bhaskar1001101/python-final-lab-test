class Passenger:
    def __init__(self, passenger_id, name, email): 
        self.passenger_id = passenger_id
        self.name = name
        self.email = email

    def get_info(self):
        return self.passenger_id, self.name, self.email

class Flight:
    def __init__(self, flight_id, departure, destination, available_seats, ticket_price):
        self.flight_id = flight_id
        self.departure = departure
        self.destination = destination
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    def check_availability(self):
        return len(self.available_seats)

    # TODO: Book Specified Seats
    def book_ticket(self, passenger : Passenger, number_of_seats : int):
        if number_of_seats <= len(self.available_seats):
            self.available_seats = self.available_seats[number_of_seats:]
            return True
        else:
            return False

    def get_ticket_price(self):
        return self.ticket_price

class FoodMenu:
    def __init__(self, menu_id, items, prices):
        self.menu_id = menu_id
        self.items = items
        self.prices = prices

    def display_menu(self):
        for item, price in zip(self.items, self.prices):
            print(f"{item} - {price}")
