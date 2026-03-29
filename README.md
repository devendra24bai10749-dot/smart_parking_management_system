## Overview
The **Smart Parking Management System** is a console-based Python application that automates vehicle parking operations such as entry, exit, fee calculation, and record management using SQLite.

It simulates a real-world parking system used in malls, colleges, offices, and smart cities.


##  Problem Statement
Manual parking systems suffer from:
- Inefficient space management  
- Time wastage in finding slots  
- Errors in billing and record keeping  
- Lack of automation  

✔ This project provides an automated and efficient solution.


##  Features
- Vehicle Entry Management  
- Vehicle Exit Tracking  
- Automatic Time Calculation  
- Smart Fee Calculation System  
- SQLite Database Storage  
- View All Parking Records  
- Menu-driven Console Interface  
- Modular Python Code Structure          

## System Architecture

User Input (CLI)
↓
main.py (Controller)
↓
parking.py (Logic Layer)
↓
utils.py (Time Functions)
↓
SQLite Database
↓
Stored Records


---

## Project Structure

Smart-Parking-System/
│
├── main.py # Entry point
├── database.py # DB connection & setup
├── parking.py # Core logic (entry/exit/billing)
├── utils.py # Time utilities
│
├── data/
│ └── parking.db # SQLite database
│
├── README.md # Documentation
├── report.md # Project report


---

## Tech Stack
| Component | Technology |
|-----------|------------|
| Language  | Python  |
| Database  | SQLite  |
| Type      | Console Application |
| Concept   | OOP + File Handling |

## Working Flow

Vehicle Entry → Store Entry Time
↓
Vehicle Exit → Fetch Entry Time
↓
Calculate Duration
↓
Generate Fee
↓
Store in Database

##  Menu Options
Vehicle Entry
Vehicle Exit
Show All Records
Exit


## Fee Calculation
- Minimum charge: ₹20  
- ₹20 per hour  
- Less than 1 hour = ₹20 fixed
## Conclusion
This project demonstrates how a real-world parking system can be efficiently implemented using Python and SQLite with clean modular design.
