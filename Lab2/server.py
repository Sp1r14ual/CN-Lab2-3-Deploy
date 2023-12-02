import socket
 
server = socket.socket()
HOST = '0.0.0.0'
PORT = None
try:
    PORT = int(input("PORT: "))
    server.bind((HOST, PORT))
except:
    print("Error")
    raise SystemExit

print(f"Server is listening at {HOST}:{PORT}")

while True:
    server.listen(10)
    
    con, addr = server.accept()
    print("New connection: ", con)
    print("IP: ", addr)
    print(f"Port: {PORT}")

    data = con.recv(1024).decode()
    res = str(sum(list(map(float, data.split()))))

    con.send(res.encode())
    con.close()