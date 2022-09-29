'''
-> bash comand to copy big csv file to postgis db
-> Needed? Adapt to run as a python script
cat out.csv | psql -h localhost -p 5432 suppliers -c "COPY eupop (x, y,z) FROM STDIN WITH (FORMAT CSV, HEADER FALSE);"
'''
