from SimpleCV import *
from time import sleep
import gpio

servo_pin = "gpio2"

myCamera = Camera(prop_set={'width':480,'height':480})
myDisplay = Display(resolution=(480,480))

def delayMicroseconds(us):
	sleep(1.0*us/1000/1000)

def delay(ms):
    	sleep(1.0*ms/1000)

def setup():
	gpio.pinMode(servo_pin, gpio.OUTPUT)
	set_servo(1500)

def set_servo(x):
	duty = x	
	for j in range(20):
        	gpio.digitalWrite(servo_pin, gpio.HIGH)
        	delayMicroseconds(duty)
       		gpio.digitalWrite(servo_pin, gpio.LOW)
        	delayMicroseconds(20000-duty)

def loop():
	while not myDisplay.isDone():
		old_x = 1450
		duty = 1500
		frame = myCamera.getImage()
		faces = frame.findHaarFeatures('face')
		if faces:
			for face in faces:
				new_x = (face.points[1][0]+face.points[0][0])/2
				new_y = (face.points[3][1]+face.points[0][1])/2
				if new_x != old_x :
					if new_x > old_x :
						duty -= 50
						set_servo(duty)
					if new_x < old_x :
						duty +=50
						set_servo(duty)
				facelayer = DrawingLayer((frame.width, frame.height))
				facelayer.circle( (new_x,new_y),(face.points[3][1]-face.points[0][1])/2,color=Color.RED )
				#facelayer.circle( (face.points[0][0],face.points[0][1]),2,color=Color.RED )
				#facelayer.circle( (face.points[1][0],face.points[1][1]),2,color=Color.RED )
				#facelayer.circle( (face.points[2][0],face.points[2][1]),2,color=Color.RED )
				#facelayer.circle( (face.points[3][0],face.points[3][1]),2,color=Color.RED )
				#facebox_dim = (200,200)
				#center_point = (frame.width/2, frame.height/2)
				#facebox = facelayer.centeredRectangle(center_point,facebox_dim)
				#facelayer.text("GO", (0,0), color=Color.WHITE)
				#frame.addDrawingLayer(newlayer)
				frame.addDrawingLayer(facelayer)
				frame.applyLayers()
				frame.show()
				old_x = new_x
				old_y = new_y
		else:
			gpio.digitalWrite(servo_pin, gpio.LOW)
			#set_servo(1500)
			frame.save(myDisplay)
		sleep(.1)

def main():
    setup()
    loop()

main()
