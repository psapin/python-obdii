from obd2 import OBDConnection
#import time
#import curses

GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#use ' ls /dev/tty* ' to list available serial ports
#I am using a bluetooth OBDLink MX scantool
serialPort = '/dev/tty.OBDLinkMX-STN-SPP'

obd = OBDConnection(serialPort)

print obd.getElmInfo()

print 'Speed: ' + obd.singleByteCommand("01 0D \r") + 'km/h'
print 'Throttle Position: ' + (obd.singleByteCommand("01 11 \r")*100/255) + '%'
print 'Relative Accelerator Pedal Position: ' + (obd.singleByteCommand("01 5A \r")*100/255) + '%'
print 'Engine Coolant Temp: ' + (obd.singleByteCommand("01 05 \r")-40) + ' C'
rpmA, rpmB = obd.twoByteCommand("01 0C \r")
print 'RPM: ' + ((rpmA*256)+rpmB)/4
runTimeA, runTimeB = obd.twoByteCommand("01 1F \r")
print 'Run Time Since Engine Start: ' + ((runTimeA*256)+runTimeB) + ' seconds'



'''def pbar(window):
#    for i in range(10):
#        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
#        window.refresh()
#        time.sleep(0.5)

#curses.wrapper(pbar)
'''