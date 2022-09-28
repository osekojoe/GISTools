#!/usr/bin/python
import psycopg2
from config import config

def get_parts(vendor_id):
	'''given vendor_id, get parts provided by a vendor'''
	conn = None
	try:
		# read db configuration
		params = config()
		#connect to psql db
		conn = psycopg2.connect(**params)
		#create a new cursor
		cur = conn.cursor()
		#call a function
		cur.callproc('get_parts_by_vendor', (vendor_id,))
		#process the result
		row = cur.fetchone()
		while row is not None:
			print(row)
			row = cur.fetchone()
		#close db connection
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	
	if __name__ == '__main__':
		get_parts(1)
