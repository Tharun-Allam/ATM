# ATM


Pocket Bank ATM – Python Project

Pocket Bank ATM is a Python console-based application that simulates basic ATM functionalities such as PIN generation, balance enquiry, cash withdrawal, deposit, and mini statement tracking. This project helps beginners understand real-world banking logic using Python, file handling, and OOP concepts.

Features

Generate and store a 4-digit PIN

PIN verification with three attempts

Balance enquiry

Cash withdrawal with balance validation

Deposit money (limit up to 50,000)

Mini statement with date and time

Persistent data storage using text files

Transaction logging

Technologies Used

Python 3

Object-Oriented Programming (OOP)

File Handling

os module

datetime module

Files Used
File Name	Description
pin.txt	Stores ATM PIN
balance.txt	Stores account balance
statement.txt	Stores transaction history
How It Works

User generates a 4-digit PIN

PIN is verified before sensitive operations

Balance is updated after every transaction

Each transaction is logged with timestamp

Mini statement displays all transactions

How to Run

Ensure Python 3 is installed

Clone the repository or download the source code

Run the program:

python atm.py

Menu Options
1. Generate PIN
2. Balance Enquiry
3. Withdraw
4. Deposit
5. Mini Statement
6. Exit

Learning Outcomes

Understand ATM workflow logic

Implement file handling for persistence

Apply object-oriented programming concepts

Handle user input and validation

Work with date and time logging

Future Enhancements

Support for multiple user accounts

PIN encryption

GUI version using Tkinter

Database integration

Daily withdrawal limits

Author

Nagatharun Allam
