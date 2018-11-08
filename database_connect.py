#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","MesutOzil11","sys" )

# GRANT all privileges on TESTDB.* to 'Max'@'localhost' IDENTIFIED BY 'maxkim' WITH GRANT OPTION;

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# disconnect from server
db.close()