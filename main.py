import _sqlite3 as sql

class Run():
    def __init__(self):
        sqft = input("Que es su sqft count because we're creepy")
        bed = input("And sus camas?")
        bath = input("BANOS")
        desired_price = input("What do you need in money?")
        self.calculate(sqft, bed, bath, desired_price)
    def calculate(self, sqft, bed, bath, desired_price):
        self.sqft = sqft
        self.bed = float(bed)
        self.bath = float(bath)
        self.desired_price = desired_price
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        cur.execute('''Create Table if not exists main (cost integer, sqft integer, bed integer, bath integer)''')
        cur.execute('''Create Table if not exists user (desired integer, sqft integer, bed integer, bath integer''')
        cur.execute('''Insert into (cost, sqft, bed, bath) VALUES (?, ?, ?, ?)''', ())
        return "Dang your house is sick dude!\nGlad to take it from you!"

r = Run()
print(r.calculate(10000, 0, 0, 1000000))
