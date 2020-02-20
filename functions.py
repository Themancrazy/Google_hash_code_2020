import time
import datetime
import threading
from threading import Thread

def	log(tag, text):
	if(tag == 'i'):
		print("[INFO] " + get_time() + text)
	elif(tag == 'e'):
		print("[ERROR] " + get_time() + text)
	elif(tag == 's'):
		print("[SUCESS] " + get_time() + text)

def get_time():
	now = str(datetime.datetime.now())
	now = now.split(' ')[1]
	threadname = threading.currentThread().getName()
	threadname = str(threadname).replace('Thread', 'Task')
	now = '[' + str(now) + ']' + ' ' + '[' + str(threadname) + ']' + ' '
	return now

def	read_file(path):
	all_lines = []
	lines = []
	try:
		f = open(path, "r")
		file_info = f.readline()
		all_lines = f.readlines()
		f.close()

	except:
		log('e', "Couldn't locate file <" + path + '>.')

	for line in all_lines:
		lines.append(line.strip("\n"))


	return file_info, lines

