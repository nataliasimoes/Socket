import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(1)

connection, address = server.accept()
i=0
soma=0
try:
    print("Aguardando mensagem do cliente.\n")
    while True:
        require = 'Digite um número: '
        connection.send(require.encode())
        data = connection.recv(1024)
        soma+=int(data.decode())
        if not data:
            break
        print('Número recebido: %s' %data.decode())
        i+=1
        if i>=2:
            break
    connection.send(str(soma).encode())
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Outra exeption: %s" %str(e)) 
finally: 
    print('Fechando conexão.\n')
    connection.close()

