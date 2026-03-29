from database import connect
from parking import add_vehicle, exit_vehicle, show_records

def menu():
    print("\n🚗 SMART PARKING SYSTEM")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show All Records")
    print("4. Exit")

connect()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        v = input("Enter vehicle number: ")
        add_vehicle(v)

    elif choice == "2":
        v = input("Enter vehicle number: ")
        exit_vehicle(v)

    elif choice == "3":
        show_records()

    elif choice == "4":
        print("👋 Exiting System...")
        break

    else:
        print("❌ Invalid Choice")