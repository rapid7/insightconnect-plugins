import base64
import logging
import time
import json
import socket


def handler_data(recv_data):
    try:
        headers, data = recv_data.split("\r\n\r\n")
        headers = headers.split("\n")
        req_method = headers[0].strip().split()
        print('Headers: {}'.format(headers))
    except:
        logging.error("Bad HTTP request format")
        return False

    if not isinstance(req_method, list):
        logging.error("Unable to find HTTP method")
        return False

    if req_method[0] == "POST":
        try:
            data_json = json.loads(data)
        except json.decoder.JSONDecodeError:
            logging.error("Unable to decode JSON")
            return False

        try:
            for header in headers:
                if header.startswith("Authorization: "):
                   auth_header = header
                   print('Authorization: {}'.format(auth_header))
        except:
            logging.error("Missing Authorization header")
            return False

        try:
            auth = auth_header.split()[2]
            print('Token: {}'.format(auth))
        except:
            logging.error("Authorization header is incomplete")
            return False

        try:
            key = base64.b64decode(auth).decode()
        except:
            logging.error("Unable to decode base64 auth value")
            return False

        # Check Authorization
        if key == 'test:':
          if isinstance(data_json, dict) and len(data_json) > 0:
            print(data_json)
          else:
            logging.info('No data in message')
            return False
        else:
          logging.info('Authorization key did not match')
          return False
    else:
      logging.info('Not a POST Request')
      time.sleep(2)
      return False
    return False

def run():
    """Run the trigger"""
    # send a test event

    BUFF = 4096
    interval = 10
    protocol = 'http'
    endpoint = '0.0.0.0'
    tcp_port = 8080

    host = protocol + "://" + endpoint + ":" + str(tcp_port)
    print('Listening on', host)

    # Open socket server to listen for messages
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((endpoint, tcp_port))
    server.listen(5)

    while True:
      conn, addr = server.accept()
      print(conn, addr)
      recv_data = conn.recv(BUFF)
      print(recv_data)
      conn.sendall(recv_data)
      conn.close()

      # Handler receiving data
      handler_data(recv_data.decode('utf-8'))
      time.sleep(interval)

run()
