import gpio
import time

servo_pin = "gpio2"

def delayMicroseconds(us):
	time.sleep(1.0*us/1000/1000)

def delay(ms):
    time.sleep(1.0*ms/1000)

def setup():
    gpio.pinMode(servo_pin, gpio.OUTPUT)

def loop():
	duty = 0
	while True:	
		for i in range(5):
			duty +=500
			for j in range(20):
        			gpio.digitalWrite(servo_pin, gpio.HIGH)
        			delayMicroseconds(duty)
        			gpio.digitalWrite(servo_pin, gpio.LOW)
        			delayMicroseconds(20000-duty)
			delay(500)
		time.sleep(1.5)
		
		for i in range(5):
			duty -=500
			for j in range(20):
        			gpio.digitalWrite(servo_pin, gpio.HIGH)
        			delayMicroseconds(duty)
        			gpio.digitalWrite(servo_pin, gpio.LOW)
        			delayMicroseconds(20000-duty)
			delay(500)		
		time.sleep(1.5)

def main():
    setup()
    loop()

main()
