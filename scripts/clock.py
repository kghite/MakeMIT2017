"""
Main Clock Functionality
"""

from arduinoComm import *
import cv2

emotionMax = 0
emotionMin = 0
ageMin = 0
ageMax = 0
swagMin = 0
swagMax = 0

emotionFall = 0
ageFall = 0
swag = 0

if __name__ == '__main__':
	# Set up the arduino communication
	s = setupArduinoComm()

	while 1:
		# Get image
		cap = cv2.VideoCapture(0)
		ret, img = cap.read()

		# Analyze image

		# If person

		# If no person