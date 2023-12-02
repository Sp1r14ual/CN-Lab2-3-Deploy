import socket


def check_on_error(arr):
    if len(arr) != 2:
        print("Error")
        exit(1)
    try:
        float(arr[0])
        float(arr[1])
    except ValueError:
        print("Error")
        exit(1)


IP = input("Введите IP адрес сервера: ")
PORT = None

client = socket.socket()
try:
    PORT = int(input("Введите номер порта: "))
    client.connect((IP, PORT))
    print("Подключение установлено")
except:
    print(f"Unable to connect to server {IP} {PORT}")
    raise SystemExit

numbers = input("Введите 2 числа через пробел: ")

check_on_error(numbers.split(" "))

client.send(numbers.encode())
data = client.recv(1024).decode()
print("Ответ сервера:", data)
client.close()
