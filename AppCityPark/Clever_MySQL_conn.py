import mysql
import mysql.connector

#Connect to the database
mysqlConn = mysql.connector.connect(
    host = '127.0.0.1', #'bmn0p7ohukcq6xxuqudp-mysql.services.clever-cloud.com',
    user = 'root', #upfp89sjo0fd79v0',
    password = '',#'HGByo9urELWdufYqUvsG',
    database = 'homeup',#'bmn0p7ohukcq6xxuqudp',
    port = 3306
)

#Create a cursor object
CleverCursor = mysqlConn.cursor()

