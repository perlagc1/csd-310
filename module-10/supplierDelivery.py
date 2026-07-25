"""
Bacchus Winery - Group Alpha
Milestone 3: Supplier Delivery Performance Report
"""

import mysql.connector
from datetime import datetime

config = {
    "host": "localhost",
    "user": "root",
    "password": "SkyLimit88!",
    "database": "bacchus_winery",
}

def supplier_delivery_report():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = """
    SELECT 
        s.supplier_name,
        COUNT(d.delivery_id) as total_deliveries,
        SUM(CASE WHEN d.actual_delivery_date > d.expected_delivery_date THEN 1 ELSE 0 END) as late_deliveries,
        ROUND(
            (SUM(CASE WHEN d.actual_delivery_date > d.expected_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(d.delivery_id)), 
            2
        ) as late_percentage
    FROM supplier s
    JOIN delivery d ON s.supplier_id = d.supplier_id
    GROUP BY s.supplier_name
    ORDER BY late_percentage DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print("\n===== SUPPLIER DELIVERY PERFORMANCE REPORT =====")
    print(" | ".join(columns))
    print("-" * 90)
    for row in rows:
        print(" | ".join(str(value) for value in row))

    cursor.close()
    conn.close()

if __name__ == "__main__":
    supplier_delivery_report()