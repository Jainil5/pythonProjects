#implement IPC using socket
import random
from multiprocessing.connection import Client
from multiprocessing.connection import Listener
address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')
print("Connected to mustafa")
# can also snd arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
while True:
    for i in range(10):
        m=random.choice([0,1])
        conn.send(m)

