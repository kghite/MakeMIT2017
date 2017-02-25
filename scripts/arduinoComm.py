"""
Arduino Communication Methods
"""

import serial

def setupArduinoComm():
	s = serial.Serial('/dev/ttyACM0', 9600)\
	return s

def writeArduino(Serial s, str pos):
	s.write(pos);

def readArduino():
	pass