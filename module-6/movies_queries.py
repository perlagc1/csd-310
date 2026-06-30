import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",   # the password you just used
    database="movies"
)

cursor = db.cursor()

# 1. Select all fields from studio table
print("\n-- DISPLAYING STUDIO RECORDS --")
cursor.execute("SELECT * FROM studio")
for studio in cursor.fetchall():
    print(studio)

# 2. Select all fields from genre table
print("\n-- DISPLAYING GENRE RECORDS --")
cursor.execute("SELECT * FROM genre")
for genre in cursor.fetchall():
    print(genre)

# 3. Movie names with runtime less than 2 hours
print("\n-- DISPLAYING SHORT FILMS (UNDER 2 HOURS) --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
for film in cursor.fetchall():
    print(f"Film Name: {film[0]}\nRuntime: {film[1]} minutes\n")

# 4. Film names grouped by director
print("\n-- DISPLAYING FILMS GROUPED BY DIRECTOR --")
print("\n-- DISPLAYING FILMS GROUPED BY DIRECTOR --")
cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
for film in cursor.fetchall():
    print(f"Director: {film[0]}\nFilm: {film[1]}\n")
for film in cursor.fetchall():
    print(f"Director: {film[0]}\nFilm: {film[1]}\n")
db.close()