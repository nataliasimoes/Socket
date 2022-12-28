import socket
import threading

# Função que realiza a soma dos números recebidos e recebe a conexão como parâmetro
def sum(connection): 
    i=0
    soma=0
    while i<2:
        require = 'Digite um número: '
        connection.send(require.encode())
        data = connection.recv(1024)
        soma+=int(data.decode())
        if not data:
            break
        print('Número recebido: %s' %data.decode())
        i+=1
    connection.send(str(soma).encode()) # Envia a soma para o cliente

class sumThread(threading.Thread): # Cria uma thread para cada conexão
    def __init__(self, connection): 
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        print('Conexão estabelecida.\n')
        sum(self.connection)
        print('Fechando conexão.\n')
        self.connection.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.bind (('localhost', 7777)) 
print('Aguardando conexões.\n')
server.listen(1)

try:
    print("Aguardando mensagem do cliente.\n")
    while True:
        connection, address = server.accept() # Aceita a conexão
        newThread = sumThread(connection) # Cria  uma nova thread para a conexão
        newThread.start() # Inicia a thread e chamada a função sum
        
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Outra exeption: %s" %str(e)) 
finally: 
    print('Fechando conexão.\n')
    connection.close()

