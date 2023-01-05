import socket, os
from motorGPIO import carStart, carStop, carTurnLeft, carTurnRight, carBackward
from gpiozero import Button 
import time 

startButton = Button(26) 

HOST = ''
PORT = 11000
speed = 0.4 #Ranges from 0-1

while True: 
    if startButton.is_pressed: 
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((HOST, PORT))
            while True:
                try:
                    print('Listening for connection.')
                    while True:
                        data, addr = s.recvfrom(1024)
                        if not data: break
                        instruction = data.decode("utf-8")
                        print(instruction)
                        if instruction == "Start":
                            carStart(speed)
                        elif instruction == "Stop":
                            carStop()
                        elif instruction == "Left":
                            carTurnLeft(speed)
                        elif instruction == "Right":
                            carTurnRight(speed)
                        elif instruction == "Backward":
                            carBackward(speed)
                        else:
                            pass
                except ConnectionResetError:
                    print('Connection reset.')
    time.sleep(1)


         