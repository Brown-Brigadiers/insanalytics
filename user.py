import numpy

from interface import Interface
import sqlite3 as sql
# new seller class
class User(Interface):
    def __init__(self, desired_price, sqft, bed, bath):
        # takes parameters from user and initializes them
        # Interface.__init__(self)
        self.dprice = int(desired_price)
        self.sqft = int(sqft)
        self.bed = int(bed)
        self.bath = int(bath)
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS User (id integer, desired integer, sqft integer, bed integer, bath integer)''')
        conn.close()
    def databasesearch(self):
        completematch = list()
        matcheslist = list()  # all of the matches are stored under this list
        costs = list()
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        # selects all four characteristics under all four being matched by user
        cur.execute('''SELECT cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=? and bath=?''',
                    (self.dprice, self.sqft, self.bed, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        completematch.append(matches)
        # stored under matches variable
        costpersqft = list()  # list holds later cost per sqft which is calculated
        # below to for loop selects all houses where each combination of characteristics of the user's house matches the database
        cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=?''',
                    (self.dprice, self.sqft, self.bed))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bath=?''',
                    (self.dprice, self.sqft, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and bed=? and bath=?''',
                    (self.dprice, self.bed, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute('''Select cost, sqft, bed, bath from Main where bed=?''',
                    (self.bed,))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where bath=?", (self.bath,))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where sqft=? and bed=? and bath=?",
                    (self.sqft, self.bed, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where sqft=? and bath=?", (self.sqft, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where sqft=? and bed=?", (self.sqft, self.bed))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where cost=? and bath=?", (self.dprice, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where cost=? and bed=?", (self.dprice, self.bed))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bath=?",
                    (self.dprice, self.sqft, self.bath))
        matches = cur.fetchall()
        matcheslist.append(matches)
        cur.execute("Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=?",
                    (self.dprice, self.sqft, self.bed))
        matches = cur.fetchall()
        matcheslist.append(matches)
        for lst in matcheslist:
            # goes through matches list that is returned and prints each list in that list
            # print(lst)
            for lst2 in lst:
                # print("iterated:", lst2)
                sqftcost = lst2[0] / lst2[1]
                costpersqft.append(sqftcost)
                # for alst in lst:
                #     print(alst)
                # appends cost per sqft to corresponding list
        # costpersqft.append(float(lst[0] / lst[1]))
        # print(costpersqft)
        for value in costpersqft:
            # print(value * self.sqft)
            totalcost = value * self.sqft
            costs.append(totalcost)
        # print(completematch)
        conn.commit()
        return costs
    def linear_regression(self):
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        # selects ALLLL the x data that is not cost
        cur.execute('''SELECT sqft, bed, bath from Main''')
        allthedata = cur.fetchall()
        print(allthedata)
        array = numpy.array(allthedata)
        print(array)