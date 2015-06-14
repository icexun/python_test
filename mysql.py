# encodeing: utf-8
#!/usr/bin/python

__author__ = 'ice'

import MySQLdb
import sys, traceback

def version():
    db = MySQLdb.connect("192.168.1.111", "root", "19851202", "test1")
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print "mysql version is: %s" % data
    db.close()

def create():
    db = MySQLdb.connect("192.168.1.111", "root", "19851202", "test1")
    cursor = db.cursor()
    cursor.execute("drop table if EXISTS employee;")
    sql = """create table employee (
             FIRST_NAME CHAR(20) NOT NULL,
             LAST_NAME CHAR(20),
             age INT,
             sex CHAR (1),
             income FLOAT )"""
    cursor.execute(sql)
    db.close()

def insert():
    db = MySQLdb.connect("192.168.1.111", "root", "19851202", "test1")
    cursor = db.cursor()
    sql = """insert into employee (first_name, last_name,age, sex, income)
             VALUES ('Mac', 'Mohan', 20, 'M', 10000)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "failed to insert"
        traceback.print_exception()
        db.rollback()
    db.close()

def select():
    db = MySQLdb.connect("192.168.1.111", "root", "19851202", "test1")
    cursor = db.cursor()
    sql = """select * from employee"""
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        #for d in data:
        #    fname = d[0]
        #    lname = d[1]
        print data
    except:
        print "Error: failed to fetch data"
    db.close()

if __name__ == "__main__":
    #version()
    #insert()
    select()
