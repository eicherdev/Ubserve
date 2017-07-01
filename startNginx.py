import subprocess, pickle, time
from collections import Counter

def startNginx():
	ls_output = subprocess.call('systemctl start nginx', shell=True)

def stopNginx():
	ls_output = subprocess.call('systemctl stop nginx', shell=True)

def restartNginx():
	ls_output = subprocess.call('systemctl restart nginx', shell=True)

def statusNginx():
	ls_output = subprocess.call('systemctl status nginx', shell=True)

def collectLog():
	connections = pickle.load( open( "save.p", "rb") )
	try:
		while True:
			with open("nginx.log") as l:
				data = l.readlines()
				for conn in data:
					conn = conn.split(" ")
					connections[conn[0]] += 1
			with open("nginx.history", "a") as h:
				for conn in data:
					h.write(conn)
			ls_output = subprocess.call('truncate -s 0 nginx.log', shell=True)
			print connections
			time.sleep(10)
	except KeyboardInterrupt:
		print 'Exiting'
		pickle.dump( connections, open( "save.p", "wb" ) )
		print 'Log saved'