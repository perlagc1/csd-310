"""
Bacchus Winery - Group Alpha
Milestone #2: Display the data in each table.

Connects to the bacchus_winery MySQL database and prints
every row from each table.
"""

import mysql.connector

# ---- Update these to match your MySQL setup ----
config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password_here",
    "database": "bacchus_winery",
}

# Tables to display, in a sensible reading order
tables = [
    "department",
    "employee",
    "work_hour",
    "supplier",
    "supply",
    "delivery",
    "wine",
    "distributor",
    "wine_order",
]


def display_table(cursor, table_name):
    """Print all rows of one table with its column headers."""
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print(f"\n===== {table_name.upper()} =====")
    print(" | ".join(columns))
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(value) for value in row))
    print(f"({len(rows)} rows)")


def main():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for table in tables:
        display_table(cursor, table)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
