import numpy
from user import User
import sqlite3 as sql
class Calculate(User):
    def __init__(self, dprice, sqft, bed, bath):
        User.__init__(self, dprice, sqft, bed, bath)
        # initializes with User's values

