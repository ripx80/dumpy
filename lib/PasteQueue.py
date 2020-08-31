from queue import *
import logging
import time
from lib.helper import check_paste
from os import path
from settings import *

class RQueue(Queue):
	
	def monitor(self):
		print('start')
		self.update()
		while(1):
			while not self.empty():
				paste = self.get()
				self.ref_id = paste.id
				logging.debug('[*] Checking ' + paste.url)
				paste.text = self.get_paste_text(paste)
				tweet = check_paste(paste)
				if tweet:
					logging.info('[*] Interesting Paste: '+tweet)	
					if SAVE:
						if not path.exists(SAVE+'/'+paste.id):
							with open(SAVE+'/'+paste.id, "w") as fp:
								fp.write(paste.text)
			self.update()
			while self.empty():
				logging.debug('[*] No results... sleeping')
				time.sleep(self.sleep)
				self.update()


        
