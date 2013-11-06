from obd2 import OBDConnection
import time
import curses

GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#use ' ls /dev/tty* ' to list available serial ports
#I am using a bluetooth OBDLink MX scantool
serialPort = '/dev/tty.OBDLinkMX-STN-SPP'

def cursesSetup(window):
	#window.addstr(0,0, 'ELM Support: ')
	window.addstr(3,0, 'Speed (km/hr): ')
	window.addstr(4,0, 'RPM: ')
	window.addstr(6,0, 'Throttle Position %: ')
	window.addstr(7,0, 'Engine Coolant Temp: ')
	window.addstr(8,0, 'Run Time Since Engine Start: ')
	window.refresh()

def main(window, obd):
	cursesSetup(window)
	window.addstr(0,13, obd.getElmInfo())
	window.refresh()
	#print 'ELM Support: \n' + obd.getElmInfo()
	#obd.sendRawCommand("AT@1 \r")
	while(True):	
		window.addstr(3,15, str(obd.oneByteCommand("01 0D \r")))
		window.refresh()
		rpmA, rpmB = obd.twoByteCommand("01 0C \r")
		window.addstr(4,5, str(((rpmA*256)+rpmB)/4))
		window.refresh()
		window.addstr(6,21, str((obd.oneByteCommand("01 11 \r")*100/255)))
		window.refresh()
		window.addstr(7,21, str((obd.oneByteCommand("01 05 \r")-40)) + ' C')
		window.refresh()
		runTimeA, runTimeB = obd.twoByteCommand("01 1F \r")
		window.addstr(8,29, str(((runTimeA*256)+runTimeB)) + ' seconds')
		window.refresh()

obdLink = OBDConnection(serialPort)
curses.wrapper(main, obdLink)
	#print 'Relative Accelerator Pedal Position: ' + (obd.oneByteCommand("01 5A \r")*100/255) + '%'
	#print 'Speed: ' + str(obd.oneByteCommand("01 0D \r")) + ' km/h'
	#print 'Throttle Position: ' + str((obd.oneByteCommand("01 11 \r")*100/255)) + '%'

	#print 'Engine Coolant Temp: ' + str((obd.oneByteCommand("01 05 \r")-40)) + ' C'
	#rpmA, rpmB = obd.twoByteCommand("01 0C \r")
	#print 'RPM: ' + str(((rpmA*256)+rpmB)/4)
	#runTimeA, runTimeB = obd.twoByteCommand("01 1F \r")
	#print 'Run Time Since Engine Start: ' + str(((runTimeA*256)+runTimeB)) + ' seconds'



'''def pbar(window):
#    for i in range(10):
#        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
#        window.refresh()
#        time.sleep(0.5)

#curses.wrapper(pbar)
'''