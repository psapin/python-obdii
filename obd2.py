
#import time
#import curses
import serial

GREEN = '\033[92m'
BLUE = '\033[94m'
HEADER = '\033[95m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

ser = None

ser_name = '/dev/tty.OBDLinkMX-STN-SPP'

def connectSerial(serialName):
	print GREEN + 'Opening serial connection on ' + BLUE + serialName + ENDC
	try:
		ser = serial.Serial(serialName, 38400, timeout=3)
		print GREEN + 'Successfully connected to ' + serialName + '!' + ENDC
	except OSError:
		print RED + 'Could not connect! Aborting!' + ENDC
		exit()

def getElmInfo():
	try:
		ser.write("ATI\r")
		data = ser.readline()
		print data
		speed_hex = data.split(' ')
		print speed_hex
		return str(data)
	except OSError:
		print RED + 'Command timed out!' + ENDC

def oneByteCommand(command):
	try:
		ser.write(command)
		data = ser.readline()
		print data
		split_data = data.split(' ')
		print split_data
		byteA = float(int('0x'+split_data[4], 0 ))
		print byteA
		return byteA
	except OSError:
		print RED + 'Command timed out!' + ENDC

def twoByteCommand(command):
	try:
		ser.write(command)
		data = ser.readline()
		print data
		split_data = data.split(' ')
		print split_data
		byteA = float(int('0x'+split_data[4], 0 ))
		print byteA
		return byteA
	except OSError:
		print RED + 'Command timed out!' + ENDC


connectSerial(ser_name)
print getElmInfo()

print 'Speed: ' + singleByteCommand("01 0D \r") + 'km/h'
print 'Throttle Position: ' + (singleByteCommand("01 11 \r")*100/255) + '%'
print 'Relative Accelerator Pedal Position: ' + (singleByteCommand("01 5A \r")*100/255) + '%'
print 'Engine Coolant Temp: ' + (singleByteCommand("01 05 \r")-40) + '°C'
rpmA, rpmB = twoByteCommand("01 0C \r")
print 'RPM: ' + ((rpmA*256)+rpmB)/4
runTimeA, runTimeB = twoByteCommand("01 1F \r")
print 'Run Time Since Engine Start: ' + ((runTimeA*256)+runTimeB) + ' seconds'




'''def pbar(window):
#    for i in range(10):
#        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
#        window.refresh()
#        time.sleep(0.5)

#curses.wrapper(pbar)



#print 'writing 01 0D'
#ser.write("01 0D \r")
#data = ser.readline()
#print 'read '+data
#speed_hex = data.split(' ')
#print speed_hex
#print 'read'+speed_hex
#speed = float(int('0x'+speed_hex[4], 0 ))
#print 'Speed: ', speed, 'km/h'

print 'writing 01 11'
ser.write("01 11 \r")
data = ser.readline()
print 'read '+data
throttle_hex = data.split(' ')
print throttle_hex
#print 'read'+throttle_hex
throttle = float(int('0x'+throttle_hex[4], 0 ))
throttle = throttle*100/255
print 'Throttle: ', throttle, '%'

print 'writing 01 0C'
ser.write("01 0C \r")
data = ser.readline()
print 'read '+data
rpm_hex = data.split(' ')
print rpm_hex
#print 'read'+rpm_hex
rpmA = float(int('0x'+rpm_hex[4], 0 ))
rpmB = float(int('0x'+rpm_hex[5], 0 ))
rpm = ((rpmA*256)+rpmB)/4
print 'RPM: ', rpm
'''

