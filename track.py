# "cook" short for chinook, just trying to be creative IDK

import sqlite3

conn = sqlite3.connect('chinook.sqlite')
cook = conn.cursor()

DELETE FROM cook
WHERE Grunge IS NULL;

SELECT * FROM cook;
                       
