import string,time,datetime,serial

BaudRate = 9600
keypadLocation = "/dev/ttyACM0"
motorLocation = "/dev/ttyACM1"

keypad = serial.Serial(keypadLocation,BaudRate)
motor = serial.Serial(motorLocation,BaudRate)

time.sleep(2)
keypad.flush()
motor.flush()

currentTime = datetime.datetime.now()
print(keypad.write(currentTime.strftime("%H, %M, %S, %d, %m, %Y")))
print(motor.write(currentTime.strftime("%H, %M, %S, %d, %m, %Y")))
#keypad.flush()

stuff =	{
	'0'  : "NORMAL", \
	'1'  : "CHECK_ID", \
	'2'  : "READ",\
	'3'  : "SET", \
	'4'  : "TEACHER", \
	'5'  : "GOOD", \
	'6'  : "WRONG", \
	'7'  : "WAKE_UP",\
	'8'  : "GET_TIME", \
	'9'  : "RESET", \
	'10' : "UNKNOWN"
	}
namesID = {
	"123"  : "Eric", \
	"456"  : "Sachin", \
	"789"  : "Anita",\
	"321"  : "Joel", \
	"654"  : "Prof Leonard", \
	"987"  : "Prof Soules"
	}

#t = str(keypad.read())
#print t

try:
	comm = stuff[str(keypad.read())]
	if comm == "WAKE_UP":
		print(keypad.write('1'))
		print(motor.write('1'))

except KeyError:
	print "Error!!!"


try:
	name = namesID[(keypad.read(3))]
	if name:
		print(keypad.write('5'))
		time.sleep(2)
		print(keypad.write(name))
except KeyError:	
	print(keypad.write('6'))

mode = stuff[str(keypad.read())]

if mode == "READ":		#Change this to call a read mode function?
	print(keypad.write('2'))
	print(motor.write('2'))
	readTime = keypad.read(5)

# Check time entered for correctness and send appropriate signal.
# Create a readtime function

	if readTime:
		print(keypad.write('5'))
	else:
		print(keypad.write('6'))
	
	time.sleep(30)

	print(keypad.write('0'))
	
elif mode == "SET":		#Change this to call a set mode function?
	print(keypad.write('3'))
	print(motor.write('2'))
	time.sleep(2)
	tme = currentTime.strftime("%H, %M")
	print(keypad.write(str(tme)))
	time.sleep(60)
	print(keypad.write('0'))

	
