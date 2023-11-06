# Importing config.py and classes.py
import config
import classes
import schema

# Database Interactions (SQLite3)
import sqlite3
from sqlite3 import Error

# Create Connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Established to SQLite3 Database")
    except Error as e:
        # For Debugging Purposes Only
        # print(e)
        print(config.error_message)
    return conn

# Create Connection
conn = create_connection(config.db_file)

# Create Table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table Created Successfully")
    except Error as e:
        print(e)

# Insert Data
def insert_data(conn, insert_data_sql, data):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql, data)
        print("Data Inserted Successfully")
    except Error as e:
        print(e)

# Select Data
def select_data(conn, select_data_sql):
    try:
        c = conn.cursor()
        c.execute(select_data_sql)
        rows = c.fetchall()
        return rows
        # for row in rows:
        #     print(row)
    except Error as e:
        print(e)

# Update Data
def update_data(conn, update_data_sql):
    try:
        c = conn.cursor()
        c.execute(update_data_sql)
        print("Data Updated Successfully")
    except Error as e:
        print(e)

def create_flights():
    # Data for initial testing
    # To be updated later
    # flight_id, departure, destination, available_seats : List, ticket_price : integer
    flight1 = classes.Flight(101, "Mumbai", "Delhi", [1, 2, 3, 4, 5], 5000)
    flight2 = classes.Flight(102, "Delhi", "Mumbai", [1, 2, 3, 4, 5], 5000)
    flight3 = classes.Flight(103, "Mumbai", "Chennai", [1, 2, 3, 4, 5], 5000)

    # Create Table
    create_table(conn, schema.flights_schema)

    # Insert Data
    flight_data_1 = (flight1.flight_id, flight1.departure, flight1.destination, str(flight1.available_seats), flight1.ticket_price)  
    flight_data_2 = (flight2.flight_id, flight2.departure, flight2.destination, str(flight2.available_seats), flight2.ticket_price)
    flight_data_3 = (flight3.flight_id, flight3.departure, flight3.destination, str(flight3.available_seats), flight3.ticket_price)
    flights_data = [flight_data_1, flight_data_2, flight_data_3]
    for flight_data in flights_data:
        insert_data(conn, "INSERT INTO flights VALUES (?, ?, ?, ?, ?)", flight_data)

def create_passengers():
    # Data for initial testing
    # To be updated later
    # passenger_id, name, email

    # Create Table
    create_table(conn, schema.passengers_schema)

    # Insert Data
    passenger1 = classes.Passenger(1, "Bhaskar Metiya", "bhaskarmetiya@gmail.com")
    passengers = [passenger1]
    for passenger in passengers:
        insert_data(conn, "INSERT INTO passengers VALUES (?, ?, ?)", (passenger.passenger_id, passenger.name, passenger.email))

def create_menu():
    # Data for initial testing
    # To be updated later
    # menu_id, food_names : List, food_prices : List

    # Create Table
    create_table(conn, schema.menu_schema)

    # Insert Data
    menu1 = classes.FoodMenu(1, ["Burger", "Pizza", "Sandwich"], [100, 200, 300])
    menus = [menu1]
    for menu in menus:
        insert_data(conn, "INSERT INTO menu VALUES (?, ?, ?)", (menu.menu_id, str(menu.items), str(menu.prices)))

def display_flights():
    flights = select_data(conn, "SELECT * FROM flights")
    # Show what the user sees
    print("Available Flights:", end = "\n\n")
    for flight in flights:
        print(f"Flight ID: {flight[0]}")
        print(f"Going from {flight[1]} to {flight[2]}")
        print(f"Available Seats: {flight[3]}")
        print(f"Ticket Price: {flight[4]}")
        print("")

def display_menu():
    menu = select_data(conn, "SELECT * FROM menu")
    # Show what the user sees
    print("Available Food:")
    for food in menu:
        print(f"Food ID: {food[0]}")
        print(f"Food Names: {food[1]}")
        print(f"Food Prices: {food[2]}")
        print("")

def book_ticket(flight_id):
    # Check if flight exists
    flight = select_data(conn, f"SELECT * FROM flights WHERE flight_id = {flight_id}")
    if len(flight) == 0:
        # Flight does not exist
        print("Flight does not exist")
        return False
    else:
        # Flight exists
        flight = flight[0]
        flight = classes.Flight(flight[0], flight[1], flight[2], flight[3], flight[4])

    passenger_name = input("Enter your name: ")
    passenger_email = input("Enter your email: ")
    passenger_id = input("Enter your Aadhar ID: ")
    # TODO: Aadhar ID Validation
    # Check if passenger exists
    passenger = select_data(conn, f"SELECT * FROM passengers WHERE name = '{passenger_name}' AND email = '{passenger_email}'")
    if not passenger:
        # Passenger does not exist
        # Create new passenger
        passenger = classes.Passenger(passenger_id, passenger_name, passenger_email)
        insert_data(conn, "INSERT INTO passengers VALUES (?, ?, ?, NULL, NULL)", (passenger.passenger_id, passenger.name, passenger.email))
    else:
        # Passenger exists
        print("Welcome back", passenger[0][1])
        passenger = passenger[0]
        passenger = classes.Passenger(passenger[0], passenger[1], passenger[2])


    # Book Ticket
    number_of_seats = int(input("Enter the number of seats: "))
    if number_of_seats <= len(flight.available_seats):
        flight.available_seats = flight.available_seats[number_of_seats:]
        update_data(conn, f"UPDATE flights SET available_seats = '{str(flight.available_seats)}' WHERE flight_id = {flight_id}")
        update_data(conn, f"UPDATE passengers SET flight_id = {flight_id} WHERE passenger_id = {passenger.passenger_id}")
        print("Ticket(s) booked successfully!")
    else:
        print("We do not have that many seats available. The maximum number of seats available is", len(flight.available_seats))

