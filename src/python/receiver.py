import socket
import json
from datalogger import update_track_info

def socket_receiver():
    # Receives UDP packets and processes JSON data
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 7001
    sock.bind(('', port))
    print("Socket connected with port", port)
    receiving = True

    try:
        while receiving:
            print('\nWaiting for a message')
            data, address = sock.recvfrom(4096)
            print('Received {} Bytes of {}'.format(len(data), address))

            try:
                json_data = json.loads(data.decode('utf-8'))  # Decoding data
                # print("JSON data successfully decoded", json_data)
                update_track_info(json_data)
            except json.JSONDecodeError as e:
                print("Error when decoding JSON data!", e)
    except KeyboardInterrupt:
        print("Socket interrupted by user")
    finally:
        sock.close()  # Close socket