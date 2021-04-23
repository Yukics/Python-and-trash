import socket
import threading
from queue import Queue

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print("Port: ", port, " Open")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

print_lock = threading.Lock()
target = input('server > ')
s_port = int(input('startp > '))
f_port = int(input('finishp > '))
#s from scan

q = Queue()

for x in range(800):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(s_port,f_port):
    q.put(worker)

q.join()
