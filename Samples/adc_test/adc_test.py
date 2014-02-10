import time
from adc import analog_read

def delay(ms):
    time.sleep(1.0*ms/1000)

def setup():
		print "read channel ADC2 value ,the V-REF = 3.3V"
		delay(3000)

def loop():
    while(1):
        value = analog_read(2)
	voltage = (value * 3.3)/4096
        print ("value =  %4d"%value)
	print ("voltage =  %4.3f  V" %voltage)
	delay(100)

def main():
    setup()
    loop()

main()
