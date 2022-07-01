cmd = 'ps -e --sort=-pcpu -o pid,user,comm > /home/astolf/PycharmProjects/sistemas_operativos/sistemas_operativos/output.txt'
#pid = "awk '/Inode/ {print($4)}' datos.txt"
os.system(cmd)

#get file object
f = open("output.txt", "r")
content = f.readlines()

i = 1
required = 5

while (i <= required):
	string = content[i]
	pid = string.split().pop(0)
	user = string.split().pop(1)
	process = string.split().pop(2)
	if (user == "root"):
		priority = 1
	else:
		priority = 0

	print(pid,user,process,priority)
	i+=1

