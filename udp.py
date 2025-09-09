import socket

HOST = "192.168.137.122"  # Mets ici l'IP de ton Android
PORT = 12345          # Même port que sur Android

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Message à envoyer : ")
    server_socket.sendto(message.encode(), (HOST, PORT))
    print(f"Message envoyé à {HOST}:{PORT}")
