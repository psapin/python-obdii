import serial

GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class OBDConnection:

	ser = None

	def __init__(self, serialName):
		print PINK + 'Opening serial connection on ' + BLUE + serialName + ENDC
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
			return data[:-1]
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def sendRawCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			return data[:-1]
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def oneByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			split_data = data.split(' ')
			byteA = float(int('0x'+split_data[4], 0 ))
			return byteA
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def twoByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			split_data = data.split(' ')
			byteA = float(int('0x'+split_data[4], 0 ))
			byteB = float(int('0x'+split_data[5], 0 ))
			return byteA, byteB
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1, -1


