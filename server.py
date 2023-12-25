import socket
import threading
import json
import csv
import os
# from http_requests import handle_client_connection, write_to_csv, Account_list

# def handle_client_connection():

def register(body):
    username = body.split()[0]
    password = body.split()[1]
    with open('./password.json', 'r') as file:
        user = json.load(file)
    user.update({username: password})
    with open('./password.json', 'w') as file:
        json.dump(user, file)
    return "Success"
    
def compare(body):
    username = body.split()[0]
    password = body.split()[1]
    with open('./password.json') as file:
        user = json.load(file)
        if username in user.keys() and user[username] == password:
            return "Success"
    return "Failed"

def handle_client_connection(client_socket):
    req = client_socket.recv(4096).decode('utf-8')
    headers, _, body = req.partition('\r\n\r\n')
    req = headers.splitlines()[0]
    method, path, _ = req.split()
    if method == 'POST':
        if path == '/login':
            state = compare(body)
        if path == '/register':
            state = register(body)
    response = (
        'HTTP/1.1 200 OK\n'
        'Content-Type: text/plain\n'
        f'Content-Length: {len(state)}\n'
        'Access-Control-Allow-Origin: *\n'
        '\n'
        f'{state}'
    )
    response = response.encode()
    client_socket.sendall(response)
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 4000))
    server_socket.listen(5)
    print('Server listening on port 4000')

    try:
        while True:
            client_socket, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down the server")
    # finally:
    #     write_to_csv('account.csv', Account_list)
    #     server_socket.close()
    #     print("Closing server")

if __name__ == '__main__':
    main()
