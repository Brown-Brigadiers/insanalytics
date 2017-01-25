import _sqlite3 as sql
import numpy
from interface import Interface
from admin import Admin


# c = Calculate()
# admin = Admin()
i = Interface()
user = User(538000, 1000, 4, 3)
# user.databasesearch()
c = Calculate(user.dprice, user.sqft, user.bed, user.bath)
c.linear_regression()
# TODO make this into a UI or callable from another program
