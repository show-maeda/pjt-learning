with open('sample.html', encoding = 'utf_8' ) as f:
  reader = f.read()
  print(reader,'\n')
  reader = reader.replace('\n','')
  print(reader)