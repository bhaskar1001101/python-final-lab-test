# Define Database Schemas
# Arrays are stored as text in the database
# We should convert them to arrays when we retrieve them and convert them to text when we insert them
# We should use a different database like PostgreSQL or Redis

flights_schema = """CREATE TABLE IF NOT EXISTS flights (
        flight_id integer PRIMARY KEY,
        departure text NOT NULL,
        destination text NOT NULL,
        available_seats text NOT NULL,
        ticket_price integer NOT NULL
    );"""

# Food IDs are stored as text in the database
# It is an array of integers(IDs) that the passenger has ordered
passengers_schema = """CREATE TABLE IF NOT EXISTS passengers (
        passenger_id integer PRIMARY KEY,
        name text NOT NULL,
        email text NOT NULL,
        flight_id integer NULL,
        food_ids text NULL,
        FOREIGN KEY (flight_id) REFERENCES flights (flight_id)
    );"""

menu_schema = """CREATE TABLE IF NOT EXISTS menu (
        menu_id integer PRIMARY KEY,
        food_names text NOT NULL,
        food_prices text NOT NULL
    );"""



