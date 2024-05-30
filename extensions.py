extension = input('File name: ').strip().lower()

if extension.endswith('.gif'):
    print('image/gif')
elif extension.endswith('.jpg'):
    print('image/jpg')
elif extension.endswith('jpeg'):
    print('image/jpg')
elif extension.endswith('png'):
    print('image/png')
elif extension.endswith('pdf'):
    print('application/pdf')
elif extension.endswith('txt'):
    print('text/plain')
elif extension.endswith('zip'):
    print('application/zip')
else:
    print('application/octet-stream')