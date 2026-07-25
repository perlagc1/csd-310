"""
Bacchus Winery - Group Alpha
Milestone 3: Wine Sales and Revenue Report
"""

import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "SkyLimit88!",
    "database": "bacchus_winery",
}

def wine_sales_report():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = """
    SELECT 
        w.wine_name,
        w.wine_type,
        d.distributor_name,
        SUM(wo.quantity_ordered) as total_cases_ordered,
        ROUND(SUM(wo.quantity_ordered * w.price_per_case), 2) as total_revenue
    FROM wine_order wo
    JOIN wine w ON wo.wine_id = w.wine_id
    JOIN distributor d ON wo.distributor_id = d.distributor_id
    GROUP BY w.wine_name, w.wine_type, d.distributor_name
    ORDER BY total_revenue DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print("\n===== WINE SALES & REVENUE REPORT =====")
    print(" | ".join(columns))
    print("-" * 100)
    for row in rows:
        print(" | ".join(str(value) for value in row))

    # Optional: Grand total
    cursor.execute("SELECT ROUND(SUM(quantity_ordered * (SELECT price_per_case FROM wine WHERE wine_id = wine_order.wine_id)), 2) FROM wine_order")
    total = cursor.fetchone()[0]
    print(f"\nGRAND TOTAL REVENUE: ${total}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    wine_sales_report()