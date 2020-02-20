import sqlite3
from functions import *
from colorama import Fore, init
from threading import Thread
import threading

def	sort_file(info):
	scores = info[0].split(" ")
	all_info = info[1:]
	library_infos = []
	library_books = []
	#------------------------------------------#
	n = 0
	for i in all_info:
		if n % 2 == 0:
			library_infos.append(i.split(" "))
		else:
			library_books.append(i.split(" "))
		n += 1
	#------------------------------------------#


	#print(library_books)
	print(scores)
	print(library_books)
	print(library_infos)
	#add2DB(scores)

def	add2DB(scores):

	conn = sqlite3.connect('libraries.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS t(scores TEXT)""")

	try:
		c.execute("""INSERT INTO t (SCORES) VALUES (?)""", (scores))
	except sqlite3.Error as e:
		log('e', f"database error: {e}")
	conn.commit()
	c.close()
	conn.close()


if(__name__ == "__main__"):
	init(autoreset=True)
	log('i', Fore.CYAN + "Reading file input")
	info = read_file("a_example.txt")
	val = info[0].split(' ')
	val2 = val[2].replace("\n", "")
	log('i', Fore.CYAN + f"The file has {val[0]} books, {val[1]} libraries and {val2} days for scanning.")
	sort_file(info[1])
