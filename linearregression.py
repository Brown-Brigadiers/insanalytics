import sqlite3 as sql
import numpy
def linear_regression():
    conn = sql.connect("data.sqlite")
    cur = conn.cursor()
    # selects ALLLL the x data that is not cost
    cur.execute('''SELECT sqft, bed, bath from Main''')
    allthedata = cur.fetchall()
    cur.execute('''SELECT cost from Main''')
    cost = cur.fetchall()
    costarray = numpy.array(cost)
    array = numpy.array(allthedata)
    arraytranspose = array.transpose()
    threeby3 = numpy.dot(arraytranspose, array)
    threeby3inverse = numpy.linalg.inv(threeby3)
    threeby1 = numpy.dot(arraytranspose, cost)
    b = numpy.dot(threeby3inverse, threeby1)
    coefficients = numpy.transpose(b)

    x = numpy.array()
    x = x.transpose()
    predictioncost = numpy.dot(coefficients, x)

    # predictioncost = 0

linear_regression()