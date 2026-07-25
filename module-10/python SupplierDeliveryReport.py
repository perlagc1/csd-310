import mysql.connector

def main():
    db = mysql.connector.connect(
    host="localhost",
    user="root",          # change if needed
    password="Faustinoypgc#1",  # replace with the one that works
    database="bacchus_winery"
)

    cursor = db.cursor()

    query = """
    SELECT s.supplier_name,
           COUNT(d.delivery_id) AS TotalDeliveries
    FROM Supplier s
    LEFT JOIN Delivery d ON s.supplier_id = d.supplier_id
    GROUP BY s.supplier_name;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("Supplier Delivery Performance Report")
    print("-------------------------------------")
    for row in results:
        print(f"Supplier: {row[0]}, Total Deliveries: {row[1]}")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()