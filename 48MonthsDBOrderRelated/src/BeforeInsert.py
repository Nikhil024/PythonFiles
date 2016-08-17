'''
Created on 16-Aug-2016

@author: nikhil_mohandas
'''

import cx_Oracle
import logging
import AfterInsertAndCompare

logging.basicConfig(filename='RecordInsertedPANDAP.log',level=logging.DEBUG)
ls = []
sl = []

def connection(username):
    settings = '{}/ADMIN@localhost/XE'.format(username)
    con = cx_Oracle.connect(settings)
    cur = con.cursor()
    return cur


def FileOperation(filename,mode):
    fh = open(filename,mode)
    return fh


def BeforeInsertPANDAP():
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
                fh = FileOperation("BeforeInsertPANDAP.log","a")
                fh.write("Tablename : {} Count     : {}".format(row,j[0]))
                fh.write("\n")

def BeforeInsertPANDAK():
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
                fh = FileOperation("BeforeInsertPANDAK.log","a")
                fh.write("Tablename : {} Count     : {}".format(row,j[0]))
                fh.write("\n")



             
def main():
#     print("executing BeforeInsertPANDAP")
#     BeforeInsertPANDAP()
#     print("finished BeforeInsertPANDAP")
#     print("executing BeforeInsertPANDAK")
#     BeforeInsertPANDAK()
#     print("executing BeforeInsertPANDAK")
#     print("finished executing before insert")
    print("executing AfterInsertPANDAK")
    AfterInsertAndCompare.AfterInsertPANDAK()
    print("finished AfterInsertPANDAK")
    print("executing AfterInsertPANDAP")
    AfterInsertAndCompare.AfterInsertPANDAP()
    print("finished AfterInsertPANDAP")
    print("finished executing after insert")
    print("executing ComparisonPANDAK")
    AfterInsertAndCompare.ComparisonPANDAK()
    print("finished ComparisonPANDAK")
    print("executing ComparisonPANDAP")
    AfterInsertAndCompare.ComparisonPANDAP()
    print("finished ComparisonPANDAP")
    print("finished Comparison")
    
    
if __name__=="__main__":main()