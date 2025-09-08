me = input('Write your name: ')
res = f'{me}> Hey you! My name is {me}, what"s your?'
condition = True

While True:
    fifow = open('/tmp/fifo', w)
    fifor = open('/tmp/fifo', r)

    fifow.write(res)
    if condition:
        user = fifor.read()
        res_user = user
        condition = False
    else:
        res_user = fifor.read()

    print(f'{user}> {res_user}')
    res = me + '> ' + input('{me}> ')
