#!/usr/bin/env bash

file_path='../data/raw/telecom.sql'

# check if the file exists in the database
if [ ! -f "$file_path" ]; then
  echo  "File not found : $file_path"
  exit 1
fi

# create the telecom db if the database does not exits
createdb -T template0 telecom_db

# run the psql command to create the dump database data
psql -U leuel -d telecom_db < $file_path
