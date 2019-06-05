import time
import json
import socket

COUNT=0

def handler_data(recv_data):
    global COUNT
    headers, data = recv_data.split("\r\n\r\n")
    headers = headers.split("\n")
    req_method = headers[0].strip().split()
    
    if req_method[0] == "POST":
      data_json = json.loads(data)
      auth = data_json.get("Authorization")
      # Check Authorization
      if auth == 'blah89d9-blah-blah-blah-blahd3d4blah':
        COUNT += 1
        if 'Alert' in data_json:
          print(COUNT)
        else:
          return False
      else:
        return False
    else:
      time.sleep(2)
      return False
    return False

def run():
    """Run the trigger"""
    # send a test event

    COUNT = 0
    BUFF = 4096
    interval = 0
    protocol = 'http'
    endpoint = '0.0.0.0'
    tcp_port = 8080

    host = protocol + "://" + endpoint + ":" + str(tcp_port)
    print('Listening on', host)
    
    # Open socket server to listen for messages
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((endpoint, tcp_port))
    server.listen()

    while True:
      conn, addr = server.accept()
      recv_data = conn.recv(BUFF)
      conn.send(recv_data)
      conn.close()

      # Handler receiving data
      handler_data(recv_data.decode('utf-8'))
      time.sleep(interval)

run()
