import threading
from receiver import socket_receiver

if __name__ == '__main__':
    receiver_thread = threading.Thread(target=socket_receiver)
    receiver_thread.start()