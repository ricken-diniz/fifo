
while (w:=input('me > ')) != 'sair':
    
    print('\033[94m Waiting him receive the message... \033[0m')

    fifow = open('/tmp/fifow', 'w')
    fifow.write(w+'\n')
    fifow.flush()

    print('\033[94m Received! Waiting him write the response... \033[0m')

    fifor = open('/tmp/fifor', 'r')
    print(fifor.read())