"""
Main Clock Functionality
"""

from arduinoComm import *
from face_analysis import *
import cv2
import os

# Scale defaults
emotionMax = 4
emotionMin = 1
ageMin = 10
ageMax = 1
swagMin = 10
swagMax = 1

# Motor range defaults
emotionMaxPos = 0
emotionMinPos = 0
ageMinPos = 0
ageMaxPos = 0
swagMinPos = 0
swagMaxPos = 0

# Motor fall positions
emotionFall = 0
ageFall = 0
swagFall = 0

# Motor current positions
emotionCurr = emotionFall
ageCurr = ageFall
swagcurr = swagFall

servoSpeedDelay = 0


"""
Set hand based on face
"""
def setHands(data):
	# Parse data and map
	eGoal = map(data[0], emotionMin, emotionMax, emotionMinPos, emotionMaxPos)
	aGoal = map(data[1], ageMin, ageMax, ageMinPos, ageMaxPos)
	sGoal = map(data[2], swagMin, swagMax, swagMinPos, swagMaxPos)

	# Set hand positions
	motionThreading(eGoal, aGoal, sGoal)


"""
Map helper
"""
def map(value, leftMin, leftMax, rightMin, rightMax):
    # Set range widths
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Set left 0-1 range
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert left to right
    return rightMin + (valueScaled * rightSpan)

	
"""
Pseudothreading helper
"""
def motionThreading(eGoal, aGoal, pGoal):
	for i in range(1, max(eGoal, aGoal, pGoal)):
		if emotionCurr != eGoal:
			if emotionCurr < eGoal:
				emotionCurr+=1
				writeArduino(emotionCurr)
			else:
				emotionCurr-=1
				writeArduino(emotionCurr)
		if ageCurr != aGoal:
			if ageCurr < eGoal:
				ageCurr+=1
				writeArduino(ageCurr)
			else:
				ageCurr-=1
				writeArduino(ageCurr)
		if swagCurr != sGoal:
			if swagCurr < sGoal:
				swagCurr+=1
				writeArduino(swagCurr)
			else:
				swagCurr-=1
				writeArduino(swagCurr)



"""
Faking data behavior
"""
def fakeOut():
	pass


"""
Falling hands behavior with swing
"""
def fall():
	pass


if __name__ == '__main__':
	# Set up the arduino communication
	s = setupArduinoComm()

	for i in range (0,5):
		# Get image
		
		if os.path.exists('image.jpeg'):
			os.remove('image.jpeg')
		cap = cv2.VideoCapture(0)
		ret, img = cap.read()
		cv2.imwrite('image.jpeg', img)
		cap.release()

		# Get image analysis
		data = getFaceAnalysis('image.jpeg')
		
		#if data:
			#print data
			


		# If person
		# Go to data -> randomly fake out on age or swag

		# If no person
		# Rotate between hanging mode and time mode
