import subprocess

proc = subprocess.Popen('sensors', stdout=subprocess.PIPE)

for line in proc.stdout:
	if line.startswith('CPU Temperature'):
		print line.split("  ")[2]
