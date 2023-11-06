# Airplane Ticket and Food Booking System
# Author: Bhaskar Metiya (CSE/22035/889)
# Date: 06/11/2023

# Modules
import database as db

# User based functions
def greet_user(first_greeting = False):
    if first_greeting:
        print("Welcome to Airplane Ticket and Food Booking System")
        print("Please select an option from the menu below:")
    print("1. Book a ticket")
    print("2. Book food")
    print("3. Exit")
    print("")

# Main function
def main():
    # Create instances of Flights, Passengers, and Food
    flights = db.create_flights()
    passengers = db.create_passengers()
    menu = db.create_menu()
    
    # User Loop
    initial_greeting = True
    while True:
        greet_user(initial_greeting)
        initial_greeting = False
        user_input = input("Enter your choice: ")
        if user_input == "1":
            # Book a ticket
            db.display_flights()
            flight_id = input("Enter the flight ID: ")
            success = db.book_ticket(flight_id)
            # TODO: Prompt user to buy food if successfully bought ticket
            print("")
        elif user_input == "2":
            # Book food
            db.display_menu()
            food_id = input("Enter the food ID: ")
            passenger_name = input("Enter your name: ")
            passenger_email = input("Enter your email: ")
            db.book_food(food_id, passenger_name, passenger_email)
            print("Food booked successfully!")
            print("")
        elif user_input == "3":
            # Exit
            print("Thank you for using this Airplane Ticket and Food Booking System!")
            print("Have a nice day!")
            print("")
            break
        else:
            # Invalid input
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
