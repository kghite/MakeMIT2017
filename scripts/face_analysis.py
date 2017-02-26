import cognitive_face as CF
import json
import httplib, urllib, base64
import random


_url =  'http:///emotion/v1.0/recognize'


def getFaceAnalysis(img_url):
	""" From a face image, returns a list of scores for emotion, age, and swag """
	FACE_KEY = ' SECRET FACE KEY ' # Replace with a valid Subscription Key here.
	CF.Key.set(FACE_KEY)
	face_result = CF.face.detect(img_url, attributes="age,glasses")
	
	if len(face_result)>=1:
		
		face_result = face_result[0]
		face_attributes = face_result['faceAttributes']
		glasses = face_attributes['glasses']
		age = face_attributes['age']
		age_score = int(age/10)
		if glasses == 'SwimmingGoggles':
			swag_score = 1
		elif glasses == 'ReadingGlasses':
			swag_score = random.randint(4,6)
		elif glasses == 'SunGlasses':
			swag_score = 10
		else:
			swag_score = random.randint(2,4)

		EMOTION_KEY = 'SECRET EMOTION KEY'
		headers = {
		    'Content-Type': 'application/octet-stream',
		    'Ocp-Apim-Subscription-Key': EMOTION_KEY,
		}
		params = urllib.urlencode({
		})
		req_data = {}
		req_data['url'] = img_url
		body = json.dumps(req_data)


		pathToFileInDisk = r'/home/brenna/MakeMIT2017/scripts/image.jpeg'
		f = open(pathToFileInDisk, "rb")
		body = f.read()
		f.close()
	
		try:
			conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
			conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)	
			response = conn.getresponse("")
			emotion_result_json = response.read()
			emotion_result = json.loads(emotion_result_json)[0]
			emotion_score = int((emotion_result['scores']['happiness']-emotion_result['scores']['sadness'])*4) # To be scaled to 0-4 range
			conn.close()
			
			return [emotion_score, age_score, swag_score]
		    
		except Exception as e:
		    print 'error', e.message
		

if __name__ == '__main__':
	getFaceAnalysis('testimage.jpg')

