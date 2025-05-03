import tkinter
import tkinter.messagebox
import sqlite3
from tkinter.constants import INSERT
from venv import create

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()


def display_menu():
    print('\n----- Phonebook Menu -----')
    print('1. Creat a new entry')
    print('2. Read an entry')
    print('3. Update an entry')
    print('4. Delete an entry')
    print('5. Exit the program')

def get_menu_choice():
    choice = int(input("Enter your choice: "))

    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Error: VAlid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input("Enter your choice: "))

    return choice


def create():
    print('Creat New Entry')
    name = input("Persons's name (First and Last): ")
    number = int(input("Persons Phone Number (No spaces or symbols):"))
    insert_row(name, number)

def read():
    name = input("Enter a name to search for: ")
    num_found = display_name(name)
    print(f'{num_found} row(s) found.')

def update():
    read()

    selected_id = int(input("Select an Entry ID: "))

    name = input("Enter the new name: ")
    number = int(input("Enter the new phone number: "))

    num_updated = update_row(selected_id, name, number)
    print(f'{num_updated} row(s) updated.')

def delete():
    read()

    selected_id = int(input("Select an Entry ID to delete: "))

    sure = input("Are you sure you want to delete this entry? (y/n): ")
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')

def insert_row(name, number):
        conn = None
        try:
            conn = sqlite3.connect("phonebook.db")
            cur = conn.cursor()
            cur.execute('''INSERT INTO Entries (PersonName, PhoneNumber)
                                VALUES (?, ?)''',
                        (name, number))
            conn.commit()
        except sqlite3.Error as err:
            print('Database Error', err)
        finally:
            if conn != None:
                conn.close()

def display_name(name):
    conn = Noneresults = []
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Entries
                        WHERE lower(PersonName) == ?''',
                    (name.lower(),))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15} '
                  f'Number: {row[2]:<6}')
    except sqlite3.Error as err:
        print("Database Error", err)
    finally:
        if conn != None:
            conn.close()

    return len(results)

def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Entries
                        SET PersonName = ?, PhoneNumber = ?
                        WHERE PersonID == ?''',
                    (name, number, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print("Database Error", err)
    finally:
        if conn != None:
            conn.close()

    return num_updated

def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Entries
                        WHERE PersonID == ?''',
                    (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print("Database Error", err)
    finally:
        if conn != None:
            conn.close()

    return num_deleted

if __name__ == '__main__':
    main()
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Entries (
    PersonID INTEGER PRIMARY KEY NOT NULL,
    PersonName TEXT NOT NULL,
    PhoneNumber INTEGER NOT NULL)''')

phonebook_data = [
    ("Jack Johnson",6123578543),
    ("Clare Stumpf",6121345980),
    ("Jin Cannon",6125890065),
    ("Greyson Gilmore",6122156780),
    ("Nathan Bentz",6124713649),
]

cur.executemany('''INSERT INTO Entries (PersonName, PhoneNumber)
            VALUES (?, ?)''', phonebook_data)



# Program #2, Donovan Thompson 5/2/2025
