from socket import *
import thread
import platform
from os import system
import time 
import sys	

BUFFER = 1024
HOST = ''
PORT = 5000 


def menu():
    print 'Bem vindo'
    decisao = raw_input('Deseja Enviar algum arquivo (s) ou pressione ENTER para aguardar uma conexao ? ')
    if decisao == 's':
        system("arp -n")
        numero = raw_input('Para quantos hosts vc deseja enviar ? ')   
        while 1:
            HOST = [] 
            i = 1
            for i in range(int(numero)):
                ip = raw_input('Digite o IP que deseja enviar uma arquivo: ')
                HOST.append(ip)
            system("ls Compartilhados")
            nomearq = raw_input('Digite o Nome do arquivo que deseja enviar: ')
            cliente(HOST,nomearq)
    else:
        servidor()
    decisao = 'n'

def handler(clientsock,addr): #Conexao de outros hosts 
    while 1:
        data = clientsock.recv(BUFFER)
        arq = open('Recebidos/dados.txt','arq')
        if not data: break
        arq.write(data)
        #time.sleep(3)
        if arq.write == True:
            break
    clientsock.close()
    print addr, "Conexao finalizada"   



def servidor():
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    
    while 1:
        print 'Esperando conexao na porta' , PORT
        clientsock, addr = serversock.accept()
        print 'Conectado com :', addr
        thread.start_new_thread(handler, (clientsock, addr))

def cliente(HOST,nomearq):
    PORT = 5000
    x = 1
    cont = 0
    for x in range(int(len(HOST))):
        s = socket(AF_INET, SOCK_STREAM)
        IP = HOST[x]
        try: 
            s.connect((IP,PORT))
            print 'Arquivo enviado para o ',IP
        except Exception, e:
            print 'Nao foi possivel conectar-se com '+ HOST[x]
             
        arq = open('Compartilhados/'+ nomearq , 'r+')
        for i in arq.readlines():
            s.send(i)
        s.close()
        arq.close()
        cont = cont + 1
    menu()

#main 
menu()

    