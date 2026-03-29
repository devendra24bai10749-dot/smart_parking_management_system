from utils import current_time
from datetime import datetime
import sqlite3

RATE_PER_HOUR = 20

def add_vehicle(vehicle_no):
    conn = sqlite3.connect("data/parking.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO parking (vehicle_number, entry_time, exit_time, fee) VALUES (?, ?, ?, ?)",
        (vehicle_no, current_time(), None, None)
    )

    conn.commit()
    conn.close()
    print("✅ Vehicle Entered Successfully!")


def calculate_fee(entry_time, exit_time):
    fmt = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(entry_time, fmt)
    end = datetime.strptime(exit_time, fmt)

    hours = (end - start).seconds / 3600
    if hours < 1:
        return 20
    return round(hours * RATE_PER_HOUR, 2)


def exit_vehicle(vehicle_no):
    conn = sqlite3.connect("data/parking.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT entry_time FROM parking
        WHERE vehicle_number=? AND exit_time IS NULL
    """, (vehicle_no,))

    row = cur.fetchone()

    if row:
        entry_time = row[0]
        exit_time = current_time()
        fee = calculate_fee(entry_time, exit_time)

        cur.execute("""
            UPDATE parking
            SET exit_time=?, fee=?
            WHERE vehicle_number=? AND exit_time IS NULL
        """, (exit_time, fee, vehicle_no))

        conn.commit()
        print(f"💰 Parking Fee: ₹{fee}")
    else:
        print("❌ Vehicle not found or already exited!")

    conn.close()


def show_records():
    conn = sqlite3.connect("data/parking.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM parking")
    rows = cur.fetchall()

    print("\n📊 PARKING RECORDS")
    print("-" * 60)

    for r in rows:
        print(r)

    conn.close()