import _sqlite3 as sql

class Admin():
    def __init__(self):
        sqft = input("Square foot: \n")
        bed = input("Bed: \n")
        bath = input("Bath: \n")
        cost = input("Cost: \n")
        self.enter_data(sqft, bed, bath, cost)
    def enter_data(self, sqft, bed, bath, cost):
        self.sqft = sqft
        self.bed = float(bed)
        self.bath = float(bath)
        self.cost = cost
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute('''Create Table if not exists main (cost integer, sqft integer, bed integer, bath integer)''')
        cur.execute(''''Insert into main (cost, sqft, bed, bath) values (?, ?, ?, ?)''', (cost, sqft, bed, bath))
        conn.commit()
admin = Admin()

