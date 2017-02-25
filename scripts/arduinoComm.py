"""
Arduino Communication Methods
"""

import serial

def setupArduinoComm():
	s = serial.Serial('/dev/ttyACM0', 9600)
	return s

def writeArduino(s, pos):
	s.write(pos);

def readArduino():
	return s.readline()