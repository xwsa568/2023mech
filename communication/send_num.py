import socket

ESP32_AP_IP = "192.168.4.1"  # ESP32-C3 SoftAP IP 주소
ESP32_PORT = 80

def sendNum():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ESP32_AP_IP, ESP32_PORT))
    
    try:
        while True:
            data = input("Enter a number to send: ")  # Mac에서 보낼 숫자 입력
            client_socket.send(data.encode())
            print("Data sent:", data)
    except KeyboardInterrupt:
        client_socket.close()

