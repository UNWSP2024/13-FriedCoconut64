import tkinter
import tkinter.messagebox
import sqlite3
from tkinter.constants import INSERT

conn = sqlite3.connect('cities.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Cities (
    CityID INTEGER PRIMARY KEY NOT NULL,
    CityName TEXT NOT NULL,
    Population INTEGER NOT NULL)''')

cities_data = [
    ("New York",8335897),
    ("Los Angeles",3898747),
    ("Chicago",2720546),
    ("Houston",2302878),
    ("Phoenix",1644409),
    ("Philadelphia",1567258),
    ("San Antonio",1472909),
    ("San Diego",1381162),
    ("Dallas",1300092),
    ("San Jose",1026908),
    ("Austin",931830),
    ("Jacksonville",868031),
    ("Fort Worth",833319),
    ("Charlotte",827097),
    ("Columbus",850106),
    ("Indianapolis",853173),
    ("Seattle",684451),
    ("Denver",682545),
    ("El Paso",681124),
    ("Washington",712816)
]

cur.executemany('''INSERT INTO Cities (CityName, Population)
            VALUES (?, ?)''', cities_data)

cur.execute('SELECT CityID, CityName, Population FROM Cities LIMIT 20')

results = cur.fetchall()

for row in results:
    print(f'{row[0]:2} {row[1]:30} {row[2]:5}')

conn.commit()
conn.close()

# Program #1, Donovan Thompson 5/2/2025
