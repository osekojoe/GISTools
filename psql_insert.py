#!/usr/bin/python

import psycopg2
from config import config

def insert_vendor(vendor_name):
	''' Insert a new vendor into the vendors tables'''
	sql = """INSERT INTO vendors(vendor_name
			VALUES(%s) RETURNING vendor_id;"""
	conn = None
	vendor_id = None
	try:
		#read db config
		params = config()
		#connect to psql db
		conn = psycopg2.connect(**params)
		#create cursor
		cur = conn.cursor()
		#excute the insert statement
		cur.execute(sql, (vendor_name))
		#get the generated id back
		vendor_id = cur.fetchone()[0]
		#commit the changes
		conn.commit()
		#close the db connection
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

	return vendor_id

def insert_vendor_list(vendor_list):
	'''insert multiple vendors into the vendors table'''
	sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
	conn = None
	try:
		#read db config
		params = config()
		#connect to psql db
		conn = psycopg2.connect(**params)
		#create cursor
		cur = conn.cursor()
		#execute INSERT
		cur.executemany(sql, vendor_list)
		#commit changes
		conn.commit()
		#close db connection
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == '__main__':
	#insert one vendor
	insert_vendor("3M Co.")
	#insert multiple vendors
	insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])