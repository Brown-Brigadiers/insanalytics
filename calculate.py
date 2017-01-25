from user import User
# calculate class derived from User
class Calculate(User):
    def __init__(self, dprice, sqft, bed, bath):
        User.__init__(self, dprice, sqft, bed, bath)
        # initializes with User's values

    def linear_regression(self):
        dprice = self.dprice
        sqft = self.sqft
        bed = self.bed
        bath = self.bath
        conn = sql.connect("data.sqlite")
        cur = conn.cursor()
        # selects ALLLL the x data that is not cost
        cur.execute('''SELECT sqft, bed, bath from Main''')
        allthedata = cur.fetchall()
        print(allthedata)
