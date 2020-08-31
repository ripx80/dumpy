
from .Paste import Paste
from bs4 import BeautifulSoup
from . import helper
from time import sleep
#from settings import SLEEP_PASTEBIN
import logging
from .PasteQueue import RQueue
from settings import *


class PastebinPaste(Paste):
    def __init__(self, id):
        self.id = id
        self.headers = None
        self.url = 'http://pastebin.com/raw.php?i=' + self.id
        #call the parent init without set this name
        super(PastebinPaste, self).__init__()


class Pastebin(RQueue):
	def __init__(self, last_id=None):
		if not last_id:
			last_id = None
			self.ref_id = last_id
			self.BASE_URL = 'http://pastebin.com'
			self.sleep = SLEEP_PASTEBIN
			super(Pastebin, self).__init__()

	def update(self):
		'''update(self) - Fill Queue with new Pastebin IDs'''
		logging.info('Retrieving Pastebin ID\'s')
		results = BeautifulSoup(helper.download(self.BASE_URL + '/archive')).find_all(
		lambda tag: tag.name == 'td' and tag.a and '/archive/' not in tag.a['href'] and tag.a['href'][1:])
		new_pastes = []
		if not self.ref_id:
			results = results[:60]
		for entry in results:     
			#pastebin id like mFKVXKE4     
			paste = PastebinPaste(entry.a['href'][1:])
			# Check to see if we found our last checked URL
			if paste.id == self.ref_id:
				break
			new_pastes.append(paste)
		for entry in new_pastes[::-1]:
			logging.info('Adding URL: ' + entry.url)
			self.put(entry)

	def get_paste_text(self, paste):
		return helper.download(paste.url)
		

