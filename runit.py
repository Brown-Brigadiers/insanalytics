# import _sqlite3 as sql
# import numpy
from interface import Interface
# from admin import Admin
from user import User

# c = Calculate()
# admin = Admin()
i = Interface()
user = User(538000, 1000, 4, 3)
# user.databasesearch()
user.linear_regression()
# TODO make this into a UI or callable from another program
