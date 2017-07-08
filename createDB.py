import csv
import re
from collections import namedtuple
import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Food''')

count = 0
fail = 0
headings = []
csv_file = "en.openfoodfacts.org.products.csv"
mysql= "CREATE TABLE IF NOT EXISTS Food (id INTEGER PRIMARY KEY, "
with open(csv_file, encoding="utf8") as f:
    f_csv = csv.reader(f, delimiter='\t')
    for h in next(f_csv):
        #headings.append(re.sub('[^a-zA-Z0-9_]', '_', h))
        h = re.sub('[^a-zA-Z0-9_]', '_', h)
        h  = re.sub('^_', '', h)
        headings.append(h)
    for heading in headings:
        mysql += heading + ' TEXT, '
    mysql2 = mysql[:-2] + ")"
    cur.execute(mysql2)
    #headings = [re.sub('[^a-zA-Z_]', count, h) for h in next(f_csv)]
    Row = namedtuple('Row', headings)
    for r in f_csv:
        insert = "INSERT OR IGNORE INTO Food " + str(tuple(headings)) + " VALUES "
        try:
            row = Row(*r)
        except:
            fail += 1
            continue
        count += 1
        values = tuple(row[idx] for idx in range(len(row)))
        insert += str(values)
        try:
            cur.execute(insert)
            print (count)
        except:
            fail += 1
            continue

    conn.commit()

print (str(count) + ' records')
print (str(fail) + ' records failed inserts')
cur.close()
