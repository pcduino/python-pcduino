import gpio
from flask import Flask, render_template, request

app = Flask(__name__)

pins = {
		 'gpio0':{'name':'Red_LED','state':False},
	  	 'gpio1':{'name':'Blue_LED','state':True}
	 	}

for pin in pins:
	gpio.pinMode(pin,gpio.OUTPUT)
 	gpio.digitalWrite(pin,gpio.LOW)

@app.route("/")  
def main(): 
	for pin in pins :
		pins[pin]['state'] = gpio.digitalRead(pin)
	templateData = {
			'pins':pins
			}
	return render_template('pin.html',**templateData)

@app.route("/<changepin>/<value>")
def action(changepin,value):
	setpin = changepin
	message = " "
	deviceName = pins[setpin]['name']

	if value == "on" :  
		gpio.digitalWrite(setpin,gpio.HIGH)
		message = "turned " + deviceName + " on."

	if value == "off" :
		gpio.digitalWrite(setpin,gpio.LOW)
		message = "turned " + deviceName + " off."

	if value == "toggle" :
		gpio.digitalWrite(setpin,not gpio.digitalRead(setpin))
		message = "toggled " + deviceName + " ."

	for pin in pins:
		pins[pin]['state'] = gpio.digitalRead(pin)
	 
	templateData = {
				'message' :  message ,
				'pins' : pins
			}
	return render_template('pin.html',**templateData)

if __name__ == "__main__" :
	app.run (host='0.0.0.0',port=80,debug=True)   
