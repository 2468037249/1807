import time
from threading import Thread
def saysorry():
	print('亲爱的，我错了')
	time.sleep(2)

for i in range(5):
	#t = Thread(target=saysorry)
	#t.start()
	saysorry()
