import threading
import os

os.mkfifo('/tmp/fifow')
os.mkfifo('/tmp/fifor')

me = input('Write your name: ')
res = f'{me} > Hey you! My name is {me}, what"s your?'
condition = True

fifow = open('/tmp/fifow', 'w')
fifor = open('/tmp/fifor', 'r')
    
while True:

    fifow.write(res)
    fifow.flush()

    if condition:
        user = fifor.read()
        res_user = user
        condition = False
    else:
        res_user = fifor.read()

    print(f'{user} > {res_user}')
    res = me + '> ' + input('{me} > ')
