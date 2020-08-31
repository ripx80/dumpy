#dum.py

# Author: Rip
# Version: 1.0
# ---------------------------------------------------

#emerge -1 requests dev-python/beautifulsoup

#from lib.regexes import regexes
from lib.Pastebin import Pastebin, PastebinPaste
from lib.Slexy import Slexy, SlexyPaste
from lib.Pastie import Pastie, PastiePaste

import logging
from settings import *
import threading
from time import sleep


def monitor():
	setLog()
	check_req()
	
	
	pastebin_thread = threading.Thread(
		target=Pastebin().monitor, args=[])
	slexy_thread = threading.Thread(
		target=Slexy().monitor, args=[])
	pastie_thead = threading.Thread(
		target=Pastie().monitor, args=[])

	for thread in (pastebin_thread, slexy_thread, pastie_thead):
		thread.daemon = True
		thread.start()
	

	try:
		while(1):
			sleep(5)
	except KeyboardInterrupt:
		logging.warn('Stopped.')
	
	
	
def go_exit(signum, frame):
	for t in thd:
		t.stop()

def check_req():
	from os import path,mkdir
	if SAVE:
		if not path.exists(SAVE):
			mkdir(SAVE)
			

def setLog():
	if DEBUG: 
		level=logging.DEBUG
	else:
		level=logging.INFO
	logging.basicConfig(
		format='%(asctime)s [%(levelname)s] %(message)s', filename=log_file, level=level)
	logging.info('Monitoring...')


if __name__=="__main__":	
	monitor()
