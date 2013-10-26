
#import time
#import curses
import serial

GREEN = '\033[92m'
BLUE = '\033[94m'
HEADER = '\033[95m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'


class OBDConnection:

	ser = None

	def __init__(self, serialName):
		print GREEN + 'Opening serial connection on ' + BLUE + serialName + ENDC
		try:
			self.ser = serial.Serial(serialName, 38400, timeout=3)
			print GREEN + 'Successfully connected to ' + serialName + '!' + ENDC
		except OSError:
			print RED + 'Could not connect! Aborting!' + ENDC
			exit()

	#gets the ELM 327 version
	def getElmInfo(self):
		try:
			self.ser.write("ATI\r")
			data = self.ser.readline()
			print data
			speed_hex = data.split(' ')
			print speed_hex
			return str(data)
		except OSError:
			print RED + 'Command timed out!' + ENDC

	def oneByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			print data
			split_data = data.split(' ')
			print split_data
			byteA = float(int('0x'+split_data[4], 0 ))
			print byteA
			return byteA
		except OSError:
			print RED + 'Command timed out!' + ENDC

	def twoByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			print data
			split_data = data.split(' ')
			print split_data
			byteA = float(int('0x'+split_data[4], 0 ))
			print byteA
			return byteA
		except OSError:
			print RED + 'Command timed out!' + ENDC


