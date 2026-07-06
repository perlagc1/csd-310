import mysql.connector

def show_films(cursor, title):
    print("\n-- {} --".format(title))
    cursor.execute("""
        SELECT film.film_name AS Name,
               film.film_director AS Director,
               genre.genre_name AS Genre,
               studio.studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)
    films = cursor.fetchall()

    for film in films:
        print("Film Name:", film[0])
        print("Director:", film[1])
        print("Genre:", film[2])
        print("Studio:", film[3])
        print()

db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

cursor = db.cursor()

# DISPLAY FILMS
show_films(cursor, "DISPLAYING FILMS")

# INSERT
cursor.execute("""
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
    VALUES ('Inception', 'Christopher Nolan', 1, 1, '2010', '148');
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# UPDATE
cursor.execute("""
    UPDATE film
    SET film_director = 'Nolan'
    WHERE film_name = 'Inception';
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# DELETE
cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Inception';
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")