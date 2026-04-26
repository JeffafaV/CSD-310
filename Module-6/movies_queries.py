# Jeff Victorino
# 04/26/2026
# Module 6.2 Assignment

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
 
import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")
 
""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

# QUERY 1 — Studio Table
    print("\n-- DISPLAYING Studio RECORDS --")

    cursor.execute("SELECT studio_id, studio_name FROM studio")

    for studio_id, studio_name in cursor:
        print(f"Studio ID: {studio_id}")
        print(f"Studio Name: {studio_name}\n")

# QUERY 2 — Genre Table
    print("\n-- DISPLAYING Genre RECORDS --")

    cursor.execute("SELECT genre_id, genre_name FROM genre")

    for genre_id, genre_name in cursor:
        print(f"Genre ID: {genre_id}")
        print(f"Genre Name: {genre_name}\n")


# QUERY 3 — Films under 2 hours
    print("\n-- DISPLAYING Short Film RECORDS --")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

    for film_name, runtime in cursor:
        print(f"Film Name: {film_name}")
        print(f"Runtime: {runtime}\n")

# QUERY 4 — Films by Director (ordered)
    print("\n-- DISPLAYING Director RECORDS in Order --")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

    for film_name, director in cursor:
        print(f"Film Name: {film_name}")
        print(f"Director: {director}\n")

# CLOSE CONNECTION
    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)