import csv
import sys
import os

""" 
Inspired from github. Divides the Originial csv file (pokemon2.csv) 
into a new csv file. First, splits into a new file with reduced 
number of rows,then fills in column headers and rows. Finally, formats the csv file and is ready to use.
"""
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
pokemon2 = sys.argv[1]

pokemon2 = os.path.join(CURRENT_DIR, pokemon2)
pokemon2 = os.path.splitext(pokemon2)[0]

rows_per_csv = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

with open(pokemon2) as infile:
  reader = csv.DictReader(infile)
  header = reader.fieldnames
  rows = [row for row in reader]
  pages = []

  row_count = len(rows)
  start_index = 0
  # here, we slice the total rows into pages, each page having [row_per_csv] rows
  while start_index < row_count:
    pages.append(rows[start_index:start_index + rows_per_csv])
    start_index += rows_per_csv

  for i, page in enumerate(pages):
    with open('{}_{}.csv'.format(pokemon2, i + 1), 'w+') as outfile:
      writer = csv.DictWriter(outfile, fieldnames='Total')
      writer.writeheader()
      for row in page:
        writer.writerow(row)

    print('DONE splitting {} into {} files'.format(pokemon2, len(pages)))
   
