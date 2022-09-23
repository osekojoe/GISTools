import psycopg2
from config import config

''' Connect to the suppliers database, print out the postgresql database version'''
def connect():
	''' connect to the psql server'''
	conn = None
	try:
		# read connection params
		params = config()

		#connect to the psql server
		print('Connecting to the psql database ...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		#execute a statement
		print('PostgreSQL database version: ')
		cur.execute('SELECT version()')

		#display the postgreSQL database version
		db_version = cur.fetchone()
		print(db_version)

		#close the communication with the postgreSQL
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

if __name__=='__main__':
	connect()