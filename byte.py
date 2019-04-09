x = b'27'

y = int(x.decode()) # decode is a method on the bytes class that returns a string
type(y)
print(y)
# <class 'int'>