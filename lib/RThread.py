#!/usr/bin/python

#coding: utf8

__author__="Rip"
__date__="16.08.2013"
__copyright__="Copyleft"
__version__="1.0"

from threading import Thread
from threading import Event
from threading import Lock
from time import time


class RThread(Thread):
	def __init__(self,iv=2):
		Thread.__init__(self)
		self.setInterval(iv)
		self.ka=True
		self.lock=None
		self.ev=Event()
	
	def setLock(self,lock):
		self.lock=lock
		
	def setInterval(self,iv):
		self.iv=iv
	
	def stop(self):
		self.ka=False
		self.ev.set()

	def run(self,fuc):
		while self.ka:
			getattr(self,fuc)()			
			self.ev.wait(self.iv)	
#~ 
#~ class RThreadHandler():
	#~ 
	#~ def __init__(self,threads):
		#~ thd=[threads]
		#~ print(thd)
			#~ 
	#~ def start(self):
		#~ for t in self.thd:
			#~ t.start()
			#~ 
	#~ def clean(self):
		#~ print('clean up')
	#~ 
	#~ def go_exit(signum, frame):
		#~ for t in self.thd:
			#~ t.stop()
		#~ self.clean()	
		#~ exit(0)
