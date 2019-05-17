import csv

with open('Book.csv', encoding = 'utf_8' ) as f:
  reader = csv.reader(f)
  header = next(reader)

  for j in header:
    print(j)

  for row in reader:
    print(row)