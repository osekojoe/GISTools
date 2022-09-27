#!/usr/bin/python

import psycopg2
from config import config

def update_vendor(vendor_id, vendor_name):
	'''update vendor name based on vendor id'''
	sql = """ UPDATE vendors
			SET vendor_name = %s
			WHERE vendor_id = %s"""
	conn = None
	updated_rows = 0
	try:
		# read db configuration
		params = config()
		#connect to psql db
		conn = psycopg2.connect(**params)
		#create a new cursor
		cur = conn.cursor()
		#execute the UPDATE statement
		cur.execute(sql, (vendor_name, vendor_id))
		#get the number of updates rows
		updated_rows = cur.rowcount
		#commit the changes to the db
		conn.commit()
		# Close the db connection
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	
	return updated_rows

if __name__ == '__main__':
	update_vendor(1, "3M Corp")