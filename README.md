# 🎬 Movie Ticket Booking System

A simple **Movie Ticket Booking System built using Python and Object-Oriented Programming (OOP)**.
This project allows users to view movies, book tickets, manage bookings, search movies/bookings, update bookings, cancel tickets, and calculate bills.

## 📌 Features

* 🎥 View available movies
* 🎟️ Book movie tickets
* 👤 Store customer details
* 🔍 Search movies
* 🔍 Search customer bookings
* ✏️ Update movie details
* ✏️ Update ticket bookings
* ❌ Cancel ticket bookings
* 🗑️ Delete movies
* 💰 Calculate customer bill
* 💺 Automatically update available seats
* 📋 View all customer bookings

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* Classes and Objects
* Lists
* Functions
* Loops and Conditional Statements
* User Input

## 🧑‍💻 OOP Concepts Used

### 1. Class and Object

The project contains two main classes:

* `MovieTickets` – stores movie information.
* `User` – stores customer and booking information.

### 2. Constructor

The `__init__()` method is used to initialize movie and customer details.

### 3. Encapsulation

Movie and customer information is stored inside class objects using instance variables.

### 4. Methods

Different methods are used to display movie and customer information and perform operations.

## 📂 Project Structure

```text
Movie-Ticket-Booking-System/
│
├── movie_ticket_booking.py
└── README.md
```

## 🎞️ Default Movies

The system comes with four default movies:

| Movie ID | Movie Name | Language | Show Time | Ticket Price | Total Seats |
| -------- | ---------- | -------- | --------- | ------------ | ----------- |
| 1        | RRR        | Telugu   | 12:00 PM  | ₹150         | 300         |
| 2        | KGF        | Kannada  | 3:00 PM   | ₹200         | 200         |
| 3        | Baahubali  | Telugu   | 6:00 PM   | ₹250         | 250         |
| 4        | Pushpa     | Telugu   | 9:00 PM   | ₹300         | 300         |

## 📋 Main Menu

```text
========== MOVIE TICKET BOOKING SYSTEM ==========

1. View Movies
2. Book Ticket
3. View Bookings
4. Search Booking
5. Update Booking
6. Cancel Booking
7. Search Movie
8. Update Movie
9. Delete Movie
10. Calculate Bill
11. Exit
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your system.

Check the version:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Ticket-Booking-System.git
```

### Step 3: Open the Project

```bash
cd Movie-Ticket-Booking-System
```

### Step 4: Run the Program

```bash
python movie_ticket_booking.py
```

## 💡 Example

When a customer books tickets, the system:

1. Displays available movies.
2. Asks the customer to select a movie.
3. Checks available seats.
4. Takes customer details.
5. Calculates the total ticket price.
6. Stores the booking.
7. Updates the available seats.

For example:

```text
Enter movie name to book: RRR
Available seats: 300

Enter number of tickets: 2
Enter customer ID: 101
Enter customer name: Balaji
Enter email: balaji@example.com
Enter phone number: 9876543210

Ticket booked successfully!

Movie: RRR
Tickets: 2
Ticket Price: 150
Total Amount: 300
Available Seats: 298
```

## 🚀 Future Improvements

The project can be enhanced by adding:

* 🔐 Customer login and authentication
* 🗄️ Database connectivity using PostgreSQL/MySQL
* 💳 Online payment functionality
* 🎫 Digital ticket generation
* 📧 Email confirmation
* 📅 Multiple dates for movie shows
* 💺 Seat selection
* 🎭 Movie genre and description
* 🖥️ GUI using Tkinter
* 🌐 Web application using Flask or Django

## 🎯 Learning Objective

This project was created to practice **Python Object-Oriented Programming** and understand how classes, objects, methods, lists, and functions can be combined to build a real-world application.

## 👨‍💻 Author

**Balaji**

### ⭐ If you find this project useful, consider giving the repository a star!
