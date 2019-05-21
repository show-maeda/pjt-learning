import csv

def main( ):
  with open('csv_sample.csv', encoding = 'utf_8' ) as f:
    reader = csv.reader(f)
    header = next(reader)
    index = []
    count = 0

    for j in header:
      j = j.replace('\ufeff','')
      index .append( j )

    print( index )

    for row in reader:
      col = 0

      for j in index:
        if j == 'telno':
          print( '0' + row[col] )
        else :
          print( row[col] )

        col += 1

if __name__ == '__main__':
  main()
