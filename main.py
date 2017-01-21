import _sqlite3 as sql

#Admin class to add new houses in. This will be taken care of through web crawling and data retrieval. Only useful for testing
class Admin():
    def __init__(self):
        # At initiation of admin class, four characteristics of each house is recorded
        sqft = input("Square foot: \n")
        bed = input("Bed: \n")
        bath = input("Bath: \n")
        cost = input("Cost: \n")
        self.enter_data(cost, sqft, bed, bath)

    def enter_data(self, cost, sqft, bed, bath):
        #takes characteristics of house and writes it to database
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
        #resets all of Main table
        #only useful for debug and testing
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

#new seller class
class User():
    def __init__(self, desired_price, sqft, bed, bath):
        #takes parameters from user and initializes them
        self.dprice = int(desired_price)
        self.sqft = int(sqft)
        self.bed = int(bed)
        self.bath = int(bath)
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        #refreshes table user because only one person needs to use it right now
        cur.execute('''DROP TABLE User''')
        cur.execute('''CREATE TABLE User (desired integer, sqft integer, bed integer, bath integer)''')
        conn.close()

    def databasesearch(self):
        #connection to database
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        #selects all four characteristics under all four being matched by user
        cur.execute('''SELECT cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=? and bath=?''',
                    (self.dprice, self.sqft, self.bed, self.bath))
        matches = cur.fetchall()
        #stored under matches variable
        costpersqft = list() #list holds later cost per sqft which is calculated
        if len(matches) == 0:
            #from here until for loop is simply variations of matches that a user may get
            #TODO implement all of the variations for the matches
            cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bed=?''',
                        (self.dprice, self.sqft, self.bed))
            matches = cur.fetchall()
            if len(matches) == 0:
                cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and sqft=? and bath=?''',
                            (self.dprice, self.sqft, self.bath))
                matches = cur.fetchall()
                if len(matches) == 0:
                    cur.execute('''Select cost, sqft, bed, bath from Main where cost=? and bed=? and bath=?''',
                                (self.dprice, self.bed, self.bath))
                    matches = cur.fetchall()
                    if len(matches) == 0:
                        cur.execute('''Select cost, sqft, bed, bath from Main where bed=?''',
                                    (self.bed,))
                        matches = cur.fetchall()
        for lst in matches:
            #goes through matches list that is returned and prints each list in that list
            print(lst)
            #appends cost per sqft to corresponding list
            costpersqft.append(float(lst[0] / lst[1]))
        print(costpersqft)
        conn.commit()


# admin = Admin()
user = User(10000, 3500, 4, 3)
user.databasesearch()
#TODO make this into a UI or callable from another program
