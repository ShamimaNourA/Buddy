import socket

# Configuration
UDP_IP = "192.168.137.75"  # Remplacez par l'adresse IP de votre appareil Android
UDP_PORT = 12345           # Port UDP utilisé dans votre application Android

# Fonction pour envoyer une commande UDP
def send_udp_command(command):
    try:
        # Créer un socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Envoyer la commande
        sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
        print(f"Commande envoyée : {command}")
        
        # Fermer le socket
        sock.close()
    except Exception as e:
        print(f"Erreur lors de l'envoi de la commande : {e}")

# Menu interactif
if __name__ == "__main__":
    print("Script de commande UDP pour le robot Buddy")
    print("Commandes disponibles : avancer, reculer, gauche, droite, stop")
    
    while True:
        command = input("Entrez une commande : ").strip().lower()
        
        if command in ["avancer", "reculer", "gauche", "droite", "stop"]:
            send_udp_command(command)
        elif command == "exit":
            print("Arrêt du script.")
            break
        else:
            print("Commande non reconnue. Veuillez réessayer.")