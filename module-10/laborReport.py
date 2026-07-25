"""
Bacchus Winery - Group Alpha
Milestone 3: Employee Labor Report
"""

import mysql.connector

# Update connection details
config = {
    "host": "localhost",
    "user": "root",
    "password": "SkyLimit88!",  # Change as needed
    "database": "bacchus_winery",
}

def employee_labor_report():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = """
    SELECT 
        d.department_name,
        e.first_name,
        e.last_name,
        SUM(w.hours_worked) as total_hours,
        COUNT(w.workhour_id) as days_worked,
        ROUND(AVG(w.hours_worked), 2) as avg_hours_per_day
    FROM employee e
    JOIN department d ON e.department_id = d.department_id
    JOIN work_hour w ON e.employee_id = w.employee_id
    GROUP BY d.department_name, e.employee_id, e.first_name, e.last_name
    ORDER BY d.department_name, total_hours DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print("\n===== EMPLOYEE LABOR SUMMARY REPORT =====")
    print(" | ".join(columns))
    print("-" * 80)
    for row in rows:
        print(" | ".join(str(value) for value in row))

    cursor.close()
    conn.close()

if __name__ == "__main__":
    employee_labor_report()