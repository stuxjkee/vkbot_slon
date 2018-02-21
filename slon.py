import vk
import requests
import threading
import time
from gtts import gTTS

answered = []

session = vk.AuthSession(scope="messages, docs", app_id='5905582', user_login='vk_login', user_password='vk_pwd')
api = vk.API(session)

def go():


	messages = api('messages.get',count=5, time_offset=20)

	

	  

	if messages[1]['date'] in answered:
		print ('already')
		raise Exception('Already answered')

	msg = messages[1]['body']

	blabla = ("??? ???????: " + msg + ". ? ?? ???? ?????")
	tts = gTTS(text=blabla, lang='ru')
	tts.save("test.mp3")



	upload_url = api('docs.getUploadServer', type='audio_message')['upload_url']


	files = {'file': open('test.mp3', 'rb')}

	r = requests.post(upload_url, files=files)

	save_doc = api.docs.save(file=r.json()['file'])
	
	doc_name = ('doc' + str(save_doc[0]['owner_id']) + '_' + str(save_doc[0]['did']))
	api.messages.send(user_id=messages[1]['uid'], attachment=doc_name)
	answered.append(messages[1]['date'])

def clear_list():
	threading.Timer(20.0, clear_list).start()
	answered.clear()

while 1:
	try:
		go()
		time.sleep(5)


	except Exception:
		time.sleep(5)
		continue






