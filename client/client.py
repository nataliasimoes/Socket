import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7777))
print ('Cliente conectado.\n')

i=0
try:
    while i<2:
        message = client.recv(1024).decode()
        res = str(input(message))
        while not res.isnumeric():
            res = str(input('Digite um número: '))
        client.send(res.encode('utf-8'))
        i+=1 
    data = client.recv(1024).decode()
    print('Soma dos números: %s' %data)
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Outra exeption: %s" %str(e)) 
finally: 
    print ("Fechando conexão.\n") 
    client.close() 