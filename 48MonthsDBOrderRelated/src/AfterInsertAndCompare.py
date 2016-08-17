'''
Created on 16-Aug-2016

@author: nikhil_mohandas
'''

import cx_Oracle
import logging

logging.basicConfig(filename='RecordInsertedPANDAK.log',level=logging.DEBUG)
ls = []
sl = []

def connection(username):
    settings = '{}/ADMIN@localhost/XE'.format(username)
    con = cx_Oracle.connect(settings)
    cur = con.cursor()
    return cur

def tablename(abc):
    list(abc)
    word = abc[12:]
    tablename = word.split()
    return tablename [0] 

def FileOperation(filename,mode):
    fh = open(filename,mode)
    return fh
    

def AfterInsertPANDAK():
    cur = connection("PANDAK")
    
    query = "SELECT table_name FROM user_tables ORDER BY table_name"
    cur.execute(query)
    for i in cur.fetchall():
        #print(i[0])
        #ls.append(i[0])
        for row in i:
            query = "SELECT COUNT(*) FROM {}".format(row)
            cur.execute(query)
            for j in cur.fetchall():
                fh = FileOperation("AfterInsertPANDAK.log","a")
                fh.write("Tablename : {} Count     : {}".format(row,j[0]))
                fh.write("\n")

def AfterInsertPANDAP():
    cur = connection("PANDAP")
    
    query = "SELECT table_name FROM user_tables ORDER BY table_name"
    cur.execute(query)
    for i in cur.fetchall():
        #print(i[0])
        #ls.append(i[0])
        for row in i:
            query = "SELECT COUNT(*) FROM {}".format(row)
            cur.execute(query)
            for j in cur.fetchall():
                fh = FileOperation("AfterInsertPANDAP.log","a")
                fh.write("Tablename : {} Count     : {}".format(row,j[0]))
                fh.write("\n")


def ComparisonPANDAK():
    BeforeInsert_fh = FileOperation("BeforeInsertPANDAK.log","r")
    AfterInsert_fh = FileOperation("AfterInsertPANDAK.log","r")
    for i in BeforeInsert_fh:
        ls.append(i)
    for j in AfterInsert_fh:
        sl.append(j)
    for nums in range(len(sl)):
        if(sl[nums] not in ls):
            print("PANDAK\n---------------------------------------------------------------------------------")
            print(tablename(str(sl[nums])))
                
def ComparisonPANDAP():
    BeforeInsert_fh = FileOperation("BeforeInsertPANDAP.log","r")
    AfterInsert_fh = FileOperation("AfterInsertPANDAP.log","r")
    for i in BeforeInsert_fh:
        ls.append(i)
    for j in AfterInsert_fh:
        sl.append(j)
    for nums in range(len(sl)):
        if(sl[nums] not in ls):
            print("PANDAP\n---------------------------------------------------------------------------------")
            print(tablename(str(sl[nums])))
