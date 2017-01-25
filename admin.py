# Admin class to add new houses in. This will be taken care of through web crawling and data retrieval. Only useful for testing
class Admin(object):
    def __init__(self):
        # At initiation of admin class, four characteristics of each house is recorded
        sqft = input("Square foot: \n")
        bed = input("Bed: \n")
        bath = input("Bath: \n")
        cost = input("Cost: \n")
        self.enter_data(cost, sqft, bed, bath)

    def enter_data(self, cost, sqft, bed, bath):
        # takes characteristics of house and writes it to database
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
        # resets all of Main table
        # only useful for debug and testing
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