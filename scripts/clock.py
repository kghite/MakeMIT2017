"""
Main Clock Functionality
"""

from arduinoComm import *
import cv2

if __name__ == '__main__':
	# Set up the arduino communication
	s = setupArduinoComm()

	while 1:
		# Get image
		cap = cv2.VideoCapture(0)
		ret, img = cap.read()

		# Analyze image

		# If person -> 

		# If no person