from sys import argv
if argv.__len__() > 1:
  from requests import get, head
  h = head(argv[1]).headers.get('Content-Length', None)
  if argv.__len__() > 2: filename = argv[2]
  else: filename = argv[1].split('/')[-1]
  f = open(filename, 'wb')
  if h != None:
    r = get(argv[1], stream=True)
    wr = 0
    for chunk in r.iter_content(chunk_size=8192):
      wr += f.write(chunk)
      print('\r['+'#'*int(wr/h*30)+'-'*((h-wr)/h*30)+f'] {wr}/{h}  ',end='')
    print('done!')
    f.close()
  else:
    r = get(url)
    f.write(r.content)
    f.close()
    print('done!')
  
