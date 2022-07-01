import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import mysql.connector


class show_gui(QMainWindow):
	def __init__(self):
		super(show_gui,self).__init__()
		uic.loadUi("untitled.ui", self)
		self.enviar_cpu.clicked.connect(self.per_cpu)
		self.enviar_memoria.clicked.connect(self.per_memory)

	def per_cpu(self):

		cant_procesos = self.get_cpu.text()

		catalogo = "CPU"

		cmd = 'ps -e --sort=-pcpu -o pid,user,comm > /home/astolf/PycharmProjects/sistemas_operativos/sistemas_operativos/output.txt'

		os.system(cmd)

		# get file object
		f = open("output.txt", "r")
		content = f.readlines()

		i = 1
		required = int(cant_procesos)

		while (i <= required):
			string = content[i]
			pid = string.split().pop(0)
			user = string.split().pop(1)
			process = string.split().pop(2)
			if (user == "root"):
				priority = 1
			else:
				priority = 0

			description = process


			try:
				connection = mysql.connector.connect(host='localhost',
													 database='dsop',
													 user='root',
													 password='kodokushi')

				clean_table = "delete from uso_cpu"

				mySql_insert_query = """INSERT INTO uso_cpu( pid, nombre, descripcion, usuario, prioridad, cant_procesos, nombre_catalogo)
						                           VALUES 
						                           (%s, %s, %s, %s, %s, %s, %s) """

				record = (pid, process, description, user, priority, cant_procesos, catalogo)

				cursor = connection.cursor()
				#cursor.execute(clean_table)
				cursor.execute(mySql_insert_query, record)
				connection.commit()
				print(cursor.rowcount, "Record inserted successfully into  db")
				#self.a_enviar.setText("Enviado")
				cursor.close()

			except mysql.connector.Error as error:
				print("Failed to insert record into db {}".format(error))

			finally:
				if connection.is_connected():
					connection.close()
					print("MySQL connection is closed")

			print(pid, user, process, priority)
			i += 1

	def per_memory(self):

		cant_procesos = self.get_memoria.text()

		catalogo = "MEM"

		cmd = 'ps -e --sort=-pcpu -o pid,user,comm > /home/astolf/PycharmProjects/sistemas_operativos/sistemas_operativos/output.txt'
		# pid = "awk '/Inode/ {print($4)}' datos.txt"
		os.system(cmd)

		# get file object
		f = open("output.txt", "r")
		content = f.readlines()

		i = 1
		required = int(cant_procesos )

		while (i <= required):
			string = content[i]
			pid = string.split().pop(0)
			user = string.split().pop(1)
			process = string.split().pop(2)
			if (user == "root"):
				priority = 1
			else:
				priority = 0

			description = process

			try:
				connection = mysql.connector.connect(host='localhost',
													 database='dsop',
													 user='root',
													 password='kodokushi')

				clean_table = "delete from uso_memoria"

				mySql_insert_query = """INSERT INTO uso_memoria ( pid, nombre, descripcion, usuario, prioridad, cant_procesos, nombre_catalogo)
			                           VALUES 
			                           (%s, %s, %s, %s, %s, %s, %s) """

				record = (pid, str(process), description, user, priority, cant_procesos, catalogo)

				cursor = connection.cursor()
				#cursor.execute(clean_table)
				cursor.execute(mySql_insert_query, record)
				connection.commit()
				print(cursor.rowcount, "Record inserted successfully into Laptop table")
				#self.a_enviar.setText("Enviado")
				cursor.close()

			except mysql.connector.Error as error:
				print("Failed to insert record into Laptop table {}".format(error))

			finally:
				if connection.is_connected():
					connection.close()
					print("MySQL connection is closed")

			print(pid, user, process, priority)
			i += 1


if __name__=='__main__':
	app = QApplication(sys.argv)
	GUI = show_gui()
	GUI.show()
	sys.exit(app.exec_())



