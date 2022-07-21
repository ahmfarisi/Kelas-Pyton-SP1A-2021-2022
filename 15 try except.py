import sys
x = 5
y = 10
try:
    print(x + 'y')
except:
    print('ini bagian except')
    print(sys.exc_info())
    