movies = []
customers = []


class MovieTickets:
    def __init__(self, movie_id, name, language, showtime, ticketprize, totalseats):
        self.movie_id = movie_id
        self.name = name
        self.language = language
        self.showtime = showtime
        self.ticketprize = ticketprize
        self.totalseats = totalseats
        self.available_seats = totalseats

    def display(self):
        print("\nMovie Details")
        print("Movie ID:", self.movie_id)
        print("Name:", self.name)
        print("Language:", self.language)
        print("Show Time:", self.showtime)
        print("Ticket Price:", self.ticketprize)
        print("Total Seats:", self.totalseats)
        print("Available Seats:", self.available_seats)


class User:
    def __init__(self, customer_id, name, email, phno):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phno = phno
        self.booked_movie = None
        self.tickets_booked = 0
        self.total_amount = 0

    def display_customer(self):
        print("\nCustomer Details")
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phno)
        print("Booked Movie:", self.booked_movie)
        print("Tickets Booked:", self.tickets_booked)
        print("Total Amount:", self.total_amount)


def add_default_movies():
    movies.extend([
        MovieTickets(1, "RRR", "Telugu", "12:00 PM", 150, 300),
        MovieTickets(2, "KGF", "Kannada", "3:00 PM", 200, 200),
        MovieTickets(3, "Baahubali", "Telugu", "6:00 PM", 250, 250),
        MovieTickets(4, "Pushpa", "Telugu", "9:00 PM", 300, 300)
    ])


def display_movies():
    if not movies:
        print("No movies available")
    else:
        for movie in movies:
            movie.display()


def search_movie():
    name = input("Enter movie name: ")
    found = False

    for movie in movies:
        if movie.name.lower() == name.lower():
            movie.display()
            found = True

    if not found:
        print("Movie not found")

def update_movie():
    m = input("Enter movie name to update: ")
    found = False

    for movie in movies:
        if movie.name.lower() == m.lower():
            movie.movie_id = int(input("Enter new movie ID: "))
            movie.name = input("Enter new movie name: ")
            movie.language = input("Enter new language: ")
            movie.showtime = input("Enter new showtime: ")
            movie.ticketprize = int(input("Enter new ticket price: "))
            movie.totalseats = int(input("Enter new total seats: "))

            movie.available_seats = movie.totalseats

            print("Movie updated successfully")
            found = True
            break

    if not found:
        print("Movie not found")

def delete_movie():
    name = input("Enter movie name to delete: ")
    found = False

    for movie in movies:
        if movie.name.lower() == name.lower():
            movies.remove(movie)
            print("Movie deleted successfully")
            found = True
            break

    if not found:
        print("Movie not found")

def book_ticket():
    print("\nAvailable Movies")
    display_movies()

    movie_name = input("\nEnter movie name to book: ")

    selected_movie = None

    for movie in movies:
        if movie.name.lower() == movie_name.lower():
            selected_movie = movie
            break

    if selected_movie is None:
        print("Movie not found")
        return

    print("Available seats:", selected_movie.available_seats)

    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Invalid number of tickets")
        return

    if tickets > selected_movie.available_seats:
        print("Not enough seats available")
        return

    customer_id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    email = input("Enter email: ")
    phno = input("Enter phone number: ")

    total_amount = tickets * selected_movie.ticketprize

    customer = User(customer_id, name, email, phno)

    customer.booked_movie = selected_movie.name
    customer.tickets_booked = tickets
    customer.total_amount = total_amount

    customers.append(customer)

    selected_movie.available_seats -= tickets

    print("\nTicket booked successfully!")
    print("Movie:", selected_movie.name)
    print("Tickets:", tickets)
    print("Ticket Price:", selected_movie.ticketprize)
    print("Total Amount:", total_amount)
    print("Available Seats:", selected_movie.available_seats)

def display_bookings():
    if not customers:
        print("No bookings available")
        return

    for customer in customers:
        customer.display_customer()

def search_booking():
    customer_id = int(input("Enter customer ID: "))

    found = False

    for customer in customers:
        if customer.customer_id == customer_id:
            customer.display_customer()
            found = True
            break

    if not found:
        print("Booking not found")

def calculate_bill():
    customer_id = int(input("Enter customer ID: "))

    for customer in customers:
        if customer.customer_id == customer_id:
            print("\n----- BILL -----")
            print("Customer:", customer.name)
            print("Movie:", customer.booked_movie)
            print("Tickets:", customer.tickets_booked)
            print("Total Amount:", customer.total_amount)
            print("----------------")
            return

    print("Customer booking not found")

def cancel_ticket():
    customer_id = int(input("Enter customer ID: "))

    for customer in customers:

        if customer.customer_id == customer_id:

            movie = None

            for m in movies:
                if m.name == customer.booked_movie:
                    movie = m
                    break

            if movie:
                movie.available_seats += customer.tickets_booked

            customers.remove(customer)

            print("Booking cancelled successfully")
            return

    print("Booking not found")

def update_booking():
    customer_id = int(input("Enter customer ID: "))

    for customer in customers:

        if customer.customer_id == customer_id:

            print("Current tickets:", customer.tickets_booked)

            new_tickets = int(input("Enter new number of tickets: "))

            movie = None

            for m in movies:
                if m.name == customer.booked_movie:
                    movie = m
                    break

            if movie is None:
                print("Movie not found")
                return

            seat_difference = new_tickets - customer.tickets_booked

            if seat_difference > movie.available_seats:
                print("Not enough seats available")
                return

            movie.available_seats -= seat_difference

            customer.tickets_booked = new_tickets
            customer.total_amount = new_tickets * movie.ticketprize

            print("Booking updated successfully")
            print("New tickets:", customer.tickets_booked)
            print("New amount:", customer.total_amount)

            return

    print("Booking not found")

def main_menu():

    add_default_movies()

    while True:

        print("\n========== MOVIE TICKET BOOKING SYSTEM ==========")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Search Booking")
        print("5. Update Booking")
        print("6. Cancel Booking")
        print("7. Search Movie")
        print("8. Update Movie")
        print("9. Delete Movie")
        print("10. Calculate Bill")
        print("11. Exit")
        print("=================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            display_bookings()

        elif choice == "4":
            search_booking()

        elif choice == "5":
            update_booking()

        elif choice == "6":
            cancel_ticket()

        elif choice == "7":
            search_movie()

        elif choice == "8":
            update_movie()

        elif choice == "9":
            delete_movie()

        elif choice == "10":
            calculate_bill()

        elif choice == "11":
            print("Thank you for using Movie Ticket Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()