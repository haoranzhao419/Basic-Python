import datetime
import os
import sqlite3
import sys
import tempfile
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.saxutils
import Console


DISPLAY_LIMIT = 20


def main():
    functions = dict(c=create_account, i=increment_money, d=decrement_money, a=account_detiles, s=stop_servey, q=quit)
    filename = os.path.join(os.path.dirname(__file__), "bank9900.sdb")
    db = None
    try:
        db = connect(filename)
        valid = frozenset("cidasq")
        menu = ("(C)reate, (I)ncrement, (D)ecrement, (A)ccount, (S)top server, (Q)uit")
        while True:
            action = Console.get_menu_choice(menu, valid)
            functions[action](db)
    finally:
        if db is not None:
            db.close()
    # db = connect(filename)
    # print("success")

    # try:
    #     # db = connect(filename)
    #     valid = frozenset("cidasq")
    #     menu = ("(C)reate, (I)ncrement, (D)ecrement, (A)ccount, (S)top server, (Q)uit")
    #     while True:
    #         action = Console.get_menu_choice(menu, valid)
    #         functions[action](db)
    # finally:
    #     if db is not None:
    #         db.close()


def connect(filename):
    create = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if create:
        cursor = db.cursor()
        # cursor.execute("CREATE TABLE customer ("
        #                "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
        #                "name varchar(10) UNIQUE NOT NULL "
        #                "phone_number varchar(9) UNIQUE NOT NULL "
        #                "customer_id TEXT NOT NULL)")
        cursor.execute("CREATE TABLE customer ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "name TEXT UNIQUE NOT NULL, "
                       "phone_number INTEGER unique UNIQUE NOT NULL)")

        cursor.execute("CREATE TABLE account ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "account_number INTEGER UNIQUE NOT NULL, "
                       "balance INTEGER NOT NULL, "
                       "customer_id INTEGER NOT NULL,"
                       "FOREIGN KEY (customer_id) REFERENCES customer(id))")
        db.commit()
    return db
 # cursor.execute("SELECT id FROM customer WHERE name=?",
 #                   (account_holder,))


def create_account(db):

    account_number = input("Account Number:")
    account_holder = input("Account Holder:")
    phone_number = input("Phone Number:")
    balance = 0
    customer_id = get_and_set_customer(db, account_holder, phone_number)
    cursor = db.cursor()
    cursor.execute("INSERT INTO account "
                   "(account_number, balance, customer_id) "
                   "VALUES (?, ?, ?)",
                   (account_number, balance, customer_id))
    db.commit()


def get_and_set_customer(db, account_holder, phone_number):
    customer_id = get_customer_id(db, account_holder)
    if customer_id is not None:
        return customer_id
    cursor = db.cursor()
    cursor.execute("INSERT INTO customer (name, phone_number) VALUES (?,?)",
                   (account_holder, phone_number))
    db.commit()
    return get_customer_id(db, account_holder)


def get_customer_id(db, account_holder):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM customer WHERE name=?",
                   (account_holder,))
    fields = cursor.fetchone()
    return fields[0] if fields is not None else None

def increment_money(db):
    account_number = input("Account_number:")
    if is_account_number(db, account_number) is False:
        return account_number
    increment_money = int(input("Amount:"))
    former_money = get_balance(db, account_number)
    result_money = increment_money + former_money
    cursor = db.cursor()
    cursor.execute("UPDATE account set balance=?"
                   "where account_number=?"
                   , (result_money, account_number))
    db.commit()

def is_account_number(db, account_number):
    cursor = db.cursor()
    cursor.execute("SELECT account_number FROM account where account_number = ?",
                   (account_number,))
    fields = cursor.fetchone()
    return True if fields is not None else False

def decrement_money(db):
    account_number = input("Account_number")
    if is_account_number(db,account_number):
        return account_number
    decrement_money = int(input())
    if get_balance(db, account_number) < decrement_money:
        print("not enough")
        return decrement_money
    former_money = get_balance(db, account_number)
    result_money = former_money - decrement_money
    cursor = db.cursor()
    cursor.execute("UPDATE account set balance=?"
                   "where account_number=?",
                   (result_money, account_number))
    db.commit()

def get_balance(db, account_number):
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM account where account_number = ?",
                   (account_number,))
    fields = cursor.fetchone()
    return fields[0] if fields is not None else None

def account_detiles(db):
    account_number = input("Account Number:")
    if is_account_number(db, account_number):
        return account_number
    print("Account {0} Detailes:".format(account_number))
    cursor = db.cursor()
    cursor.execute(("select customer.name, customer.phone_number, account.balance from account and customer where account.Account_Number=?"),(account_number))
    fields = cursor.fetchone()
    print(fields)
def stop_servey(db):
    return
def quit(db):
    if db is not None:

        db.commit()
        db.close()
        print("Saved")
    sys.exit()


main()