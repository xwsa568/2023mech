import socket

ESP32_AP_IP = "192.168.4.1"  # ESP32-C3 SoftAP IP 주소
ESP32_PORT = 80

def sendNum(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ESP32_AP_IP, ESP32_PORT))
    
    try:
        client_socket.send(data.encode())
        print("Data sent:", data)
    except KeyboardInterrupt:
        client_socket.close()

