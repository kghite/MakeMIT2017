"""
Main Clock Functionality
"""
import serial
from arduinoComm import *
from face_analysis import *
import cv2
import os
from time import sleep
from PIL import Image
import scipy.ndimage
import struct
import random
import math


# Scale defaults
emotionMax = 4
emotionMin = 1
ageMin = 10
ageMax = 1
swagMin = 10
swagMax = 1

# Motor range defaults
emotionMaxPos = 40
emotionMinPos = 160
ageMinPos = 170
ageMaxPos = 50
swagMinPos = 40
swagMaxPos = 160

# Motor fall positions
emotionFall = 90
ageFall = 200
swagFall = 20

# Motor current positions
emotionCurr = emotionFall
ageCurr = ageFall
swagCurr = swagFall

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
	print [eGoal, aGoal, sGoal]
	s.write(struct.pack('>BBB', eGoal, aGoal, sGoal))

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
Falling hands behavior with swing
"""
def fall():
	s.write(struct.pack('>BBB', emotionFall, ageFall, swagFall))


"""
Faking data behavior
"""
def fakeOut():
	# Set arms to min swag, max age, min emotion
	setHands([0, 0, 0])
	sleep(5)

	fall()
	sleep(1)


"""
Fall based on Euler equations
"""
def fallGracefully(theta):
    norm = (90, 200, 20)

    dT = 0.01
    g = -9.8
    l = .125
    c = 0.2

    dTheta = [0, 0, 0]
    # dThetaEmote = 0
    # dThetaAge = 0
    # dThetaSwag = 0

    ddTheta[0, 0, 0]
    # ddThetaEmote = 0
    # ddThetaAge = 0
    # ddThetaSwag = 0
    thresh
    count = 0
    while count < 200:
        for i, q in enumerate(theta):
            nTheta = q - norm[i]
            nTheta = math.radians(nTheta + dT*dTheta[i])
            dTheta[i] = dTheta[i] + dT*ddTheta[i]
            ddTheta[i] = -g/l*math.sin(math.radians(nTheta)) - c*nTheta
            theta[i] = math.degrees(nTheta + norm[i])
        s.write(struct.pack('>BBB', theta[0], theta[1], theta[2]))
        count = count+1



def setDataFromOpenCV():
	cap = cv2.VideoCapture(0)
	if cap.isOpened():
		while 1:
			# Get image
			if os.path.exists('image.jpeg'):
				os.remove('image.jpeg')
			
			ret, img = cap.read()
			#cv2.imshow('image', img)
			#if cv2.waitKey(5):
			print ' '			
			cv2.imwrite('image.jpeg', img)
			
			# Get image analysis
			
			data = getFaceAnalysis('image.jpeg') #[emotion_score, age_score, swag_score	
			if data:
				print data
				trick = random.randint(1, 5)
				if trick == 4:
					fakeOut()
				setHands(data)
				sleep(15)
				fall()

	cap.release()

if __name__ == '__main__':
	# Set up the arduino communication
	s = serial.Serial('/dev/ttyACM0', 9600)
	while 1:
		setDataFromOpenCV()
		sleep(5)
		fall()
