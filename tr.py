#implement IPC using socket
from multiprocessing.connection import Listener
from multiprocessing.connection import Client
address = ('localhost', 6000)     
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()
print ('connected to Jainil'), listener.last_accepted
while True:
    m = conn.recv()
    print("Jainil messaged: ",m)

listener.close()