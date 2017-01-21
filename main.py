import _sqlite3 as sql


class Admin():
    def __init__(self):
        sqft = input("Square foot: \n")
        bed = input("Bed: \n")
        bath = input("Bath: \n")
        cost = input("Cost: \n")
        self.enter_data(cost, sqft, bed, bath)

    def enter_data(self, cost, sqft, bed, bath):
        self.sqft = sqft
        self.bed = bed
        self.bath = bath
        self.cost = cost
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Main (cost integer, sqft integer, bed integer, bath integer)''')
        cur.execute('''INSERT INTO Main (cost, sqft, bed, bath) VALUES (?, ?, ?, ?)''', (cost, sqft, bed, bath))
        conn.commit()
        conn.close()
    def restart(self):
        inp = input("ARE YOU SURE YOU WANT TO DO THIS? (Y/N)\n").lower()
        if inp == "y":
            inp2 = input("ARE YOU COMPLETELY SURE? YOU CANNOT GET BACK THIS MUCH DATA! (Y/N)\n").lower()
            if inp2 == "y":
                conn = sql.connect("data.sqlite")
                cur = conn.cursor()
                cur.execute('''DROP TABLE Main''')
            else:
                print("cool you didn't break everything")
                return 0
        else:
            print("nice. good job using common sense")
            return 0



class User():
    def __init__(self, desired_price, sqft, bed, bath):
        self.dprice = int(desired_price)
        self.sqft = int(sqft)
        self.bed = int(bed)
        self.bath = int(bath)
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute('''DROP TABLE User''')
        cur.execute('''CREATE TABLE User (desired integer, sqft integer, bed integer, bath integer)''')
        conn.close()
    def databasesearch(self):
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute('''SELECT cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=? and bath=?''', (self.dprice, self.sqft, self.bed, self.bath))
        matches = cur.fetchall()
        if len(matches) == 0:
            print("none")
        for lst in matches:
            print(lst)
        conn.commit()


# admin = Admin()
user = User(10000, 3500, 4, 3)
user.databasesearch()
