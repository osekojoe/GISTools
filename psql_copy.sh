#!/bin/bash
# bash comand to copy big csv file to postgis db
# dbname == suppliers; table_name == eupop
cat out.csv | psql -h localhost -p 5432 suppliers -c "COPY eupop (x, y,z) FROM STDIN WITH (FORMAT CSV, HEADER FALSE);"