import socket
import logging
import threading
import time
## Creating Keyboard Interrupt Handler function
def keyboardInterruptHandler():
    print(' Connection   closed.')
    tcp_client.close()
    

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creating a read function
def read():
    
    try:
        
        while True: 
            full_msg =''
            received = tcp_client.recv(8)
            if received=="\n":
                break
            full_msg += received.decode("utf-8")
            
            
            logger.info(format(full_msg))
            print ("Bytes Received: {}".format(full_msg))
                     
    except:
        keyboardInterruptHandler()

#create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig (filename= "C:\\Users\\SCD UM\\Desktop\\LabProjects\\ethernet-client\\Data.log", 
level = logging.DEBUG,
format = LOG_FORMAT)

logger = logging.getLogger()


host_ip = input('Give me the adresse: ')
#host_ip = socket.gethostname()
server_port = input('Give me the port number: ')
#host_ip, server_port = "192.168.137.40", 7
#data = "1"

# Initialize a TCP client socket using SOCK_STREAM
#tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host_ip, int(server_port)))
    print('Connected with the server')
    
#keep reading, to exit i use ctrl+c
    #x = 1
    #while x==1 :
        #def write():
    x=threading.Thread(target=read)#read function on it's own thread
    x.start() 
    while True :
        data = input('Give me a number: ')
        
        tcp_client.sendall(data.encode())
        logger.info(format(data))
        print ("Bytes Sent:     {}".format(data))
        time.sleep(0.5) #just to seperate when visualizing
     
finally:
    tcp_client.close()

