import serial
import time

arduino = serial.Serial('', 11520) #port num, baud rate

while 1:
    var = input()
    var = var.encode('utf-8')
    arduino.write(var)
    time.sleep(1)

