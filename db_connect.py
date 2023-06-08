#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:06:53 2023

@author: tanchaiwee
"""

import os

from mysql import connector
from dotenv import load_dotenv


#load_dotenv()
#MYSQL_ID = os.getenv("MYSQL_ID")
#MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
def db_connection():
    config = {
        'host' : "localhost",
        'user' : 'root',
        'password' : 'qwer1234',
        'database' : 'jobplanet_data'
        }
    
    
    try:
        cnx = connector.connect(**config)
    except connector.Error as err:
        if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            
    return cnx


def insert_into_db():
    sql = """INSERT INTO tmp (company_name,location,review_count,rating,average_salary) VALUES (%s, %s, %s, %s, %s)"""
    val = ('xxx', 'suwon', 20, 3.3, 4000)
    cnx = db_connection()
    #cnx.reconnect()
    cursor = cnx.cursor()
    cursor.execute(sql, val)
    cnx.commit()
    print(cursor.rowcount, "Record inserted successfully into WIKI2 table")
    # disconnect from server
    cnx.close()
    
    
def select_from_db(table):
    sql = f"SELECT * FROM {table}"
    #val = 'tmp'
    cnx = db_connection()
    #cnx.reconnect()
    cursor = cnx.cursor()
    cursor.execute(sql)
    record = cursor.fetchall()
    print(record)
    print(cursor.rowcount, "Record returned successfully from "+ table)
    # disconnect from server
    cnx.close()